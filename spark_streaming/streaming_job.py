import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from cassandra.cluster import Cluster

# ---------- Logging ----------
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# ---------- Spark ----------
def create_spark_connection():
    try:
        spark = (
            SparkSession.builder
            .appName("IntradaySalesPipeline")
            .config(
                "spark.jars.packages",
                "org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.1,"
                "com.datastax.spark:spark-cassandra-connector_2.12:3.4.1"
            )
            .config("spark.cassandra.connection.host", "localhost")  # change to "cassandra" if in Docker
            .getOrCreate()
        )
        spark.sparkContext.setLogLevel("WARN")
        logging.info("✅ Spark connection created successfully.")
        return spark
    except Exception as e:
        logging.error(f"❌ Couldn't create the Spark session: {e}")
        return None

# ---------- Cassandra Setup ----------
def ensure_keyspace_and_table():
    try:
        cluster = Cluster(['localhost'])  # change to "cassandra" if inside Docker
        session = cluster.connect()

        session.execute("""
            CREATE KEYSPACE IF NOT EXISTS intraday_sales_keyspace
            WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
        """)

        session.execute("""
            CREATE TABLE IF NOT EXISTS intraday_sales_keyspace.sales (
                transaction_id TEXT PRIMARY KEY,
                timestamp TEXT,
                region TEXT,
                category TEXT,
                sales INT
            );
        """)

        logging.info("✅ Keyspace and table ready in Cassandra.")
        session.shutdown()
        cluster.shutdown()
    except Exception as e:
        logging.error(f"❌ Failed to create keyspace/table: {e}")
        raise

# ---------- Main ----------
if __name__ == "__main__":
    spark = create_spark_connection()
    if spark is None:
        raise SystemExit(1)

    # Make sure Cassandra objects exist
    ensure_keyspace_and_table()

    # Define schema of incoming Kafka JSON
    schema = StructType([
        StructField("timestamp", StringType(), True),
        StructField("region", StringType(), True),
        StructField("category", StringType(), True),
        StructField("sales", IntegerType(), True),
        StructField("transaction_id", StringType(), True),
    ])

    # Kafka Source (real-time stream)
    kafka_df = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", "localhost:9092")  # or "broker:9092" if in Docker
        .option("subscribe", "intraday_sales")
        .option("startingOffsets", "latest")
        .load()
    )

    # Parse Kafka JSON
    parsed_df = (
        kafka_df
        .selectExpr("CAST(value AS STRING) AS json_data")
        .select(from_json(col("json_data"), schema).alias("data"))
        .select("data.*")
    )

    # Function to write each batch to Cassandra
    def write_to_cassandra(batch_df, batch_id):
        batch_df.write \
            .format("org.apache.spark.sql.cassandra") \
            .mode("append") \
            .option("keyspace", "intraday_sales_keyspace") \
            .option("table", "sales") \
            .save()
        logging.info(f"✅ Batch {batch_id} written to Cassandra successfully.")

    # Write Stream → Cassandra using foreachBatch
    query = parsed_df.writeStream \
        .foreachBatch(write_to_cassandra) \
        .option("checkpointLocation", "/tmp/checkpoints/intraday_sales") \
        .start()

    logging.info("🚀 Real-time Intraday Sales pipeline started.")
    query.awaitTermination()
