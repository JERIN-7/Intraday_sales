<img width="3274" height="1221" alt="Data engineering architecture" src="https://github.com/user-attachments/assets/a241593f-c83e-4d4c-b593-efb2ca6f76c8" />
# IntraDay Sales

This project demonstrates a complete end-to-end real-time data engineering pipeline. It captures streaming data via Apache Kafka, processes it using Apache Spark, and stores the transformed data in Cassandra for efficient querying. The workflow is orchestrated using Apache Airflow, and Superset is used for real-time data visualization and analytics. All components are fully containerized with Docker, ensuring seamless deployment, scalability, and portability across environments.






The project is designed with the following components:

**Data Source:** Streaming data is ingested in real-time via Apache Kafka.

**Apache Airflow: ** Orchestrates the entire pipeline, managing tasks such as data ingestion, processing, and loading into storage.

**Apache Kafka and Zookeeper:** Handle real-time data streaming and coordination between producers and consumers.

**Control Center and Schema Registry:** Facilitate monitoring of Kafka streams and management of message schemas.

**Apache Spark:** Processes streaming data in real-time using its master and worker nodes.

**Cassandra:** Serves as the storage layer for processed data, enabling efficient querying and analytics.

**Superset:** Provides real-time dashboards and visualizations based on the processed data.

    <img width="1536" height="1024" alt="ChatGPT Image Sep 21, 2025, 08_41_26 PM" src="https://github.com/user-attachments/assets/49b190c6-a9ee-4325-b11a-b8eadb85f18f" />

Technolgies Used

Apache Airflow
Python
Apache Kafka
Apache Zookeeper
Apache Spark
Apache Superset
Cassandra
PostgreSQL
Docker






