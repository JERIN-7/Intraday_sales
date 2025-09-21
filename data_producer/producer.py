import random
import time
import uuid
import json
from datetime import datetime
from kafka import KafkaProducer
from categories import categories, price_ranges
from regions import regions


producer  = KafkaProducer(
       bootstrap_servers=['broker:29092'],
       value_serializer = lambda v: json.dumps(v).encode("utf-8")


)

topic_name = "intraday_sales"

def generate_transactions():

    category = random.choice(categories)
    min_price , max_price = price_ranges[category]


    return{
        "timestamp" : datetime.now().isoformat(),
        "region" : random.choice(regions),
        "category" : category,
        "sales" : random.randint(min_price, max_price),
        "transaction_id" : str(uuid.uuid4())
    }


if __name__ == "__main__":
    print("🚀 Starting Kafka Producer...")  
    try:
        while True:
            for _ in range(20):
                data = generate_transactions()
                producer.send(topic_name, value=data)
                print(f"Sent: {data}")
            time.sleep(1)

    except KeyboardInterrupt:
           print("🛑 Stopping producer...")
    finally:
        producer.flush()
        producer.close()       
