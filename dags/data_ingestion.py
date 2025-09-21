from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import subprocess
from datetime import datetime, timedelta


#Kafka producer 

def run_producer():
    subprocess.run(["python3", "/opt/airflow/Intraday_sales/data_producer/producer.py"], check=True)



default_args = {
    "owner" : "jerin",
    "retries" : 1,
    "retry_delay" : timedelta(minutes =1),

}   

with DAG(
 dag_id = "intraday_sales_dag",
 default_args=default_args,
 start_date=datetime(2025,9,6),
 schedule_interval="@once",
 catchup=False,
)as dag:


   produce = PythonOperator(
    task_id="run_producer",
    python_callable=run_producer
)

  


