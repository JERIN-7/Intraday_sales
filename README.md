# **IntraDay Sales – Real-Time Data Engineering Pipeline**

This project demonstrates a **complete end-to-end real-time data engineering pipeline**. It captures streaming data via **Apache Kafka**, processes it using **Apache Spark**, and stores the transformed data in **Cassandra** for efficient querying. The workflow is orchestrated with **Apache Airflow**, while **Superset** provides real-time visualization and analytics.

All components are fully containerized with **Docker**, ensuring **seamless deployment, scalability, and portability** across environments.

---

## **Project Architecture**

<img width="100%" alt="Data Engineering Architecture" src="https://github.com/user-attachments/assets/a241593f-c83e-4d4c-b593-efb2ca6f76c8" />

The pipeline flow can be summarized as:

1. **Data Source:** Real-time streaming data ingested via **Apache Kafka**.  
2. **Apache Airflow:** Orchestrates the ETL pipeline, scheduling tasks like data ingestion, processing, and storage.  
3. **Apache Kafka & Zookeeper:** Handle **real-time streaming**, ensuring smooth coordination between producers and consumers.  
4. **Control Center & Schema Registry:** Monitor Kafka streams and manage message schemas effectively.  
5. **Apache Spark:** Performs **real-time processing**, transformations, and aggregations on the streaming data.  
6. **Cassandra:** Stores processed data for **fast and scalable querying**.  
7. **Superset:** Visualizes the processed data through **interactive dashboards**, enabling real-time insights.

---

## **Technologies Used**

| Technology | Purpose |
|------------|---------|
| **Python** | Programming language for ETL scripts, Spark jobs, and Kafka producers/consumers |
| **Apache Airflow** | Orchestration and workflow management |
| **Apache Kafka** | Real-time data streaming |
| **Apache Zookeeper** | Kafka cluster coordination |
| **Control Center & Schema Registry** | Kafka monitoring & schema management |
| **Apache Spark** | Distributed data processing |
| **Cassandra** | NoSQL database for fast analytics |
| **PostgreSQL** | Storage for raw or historical data |
| **Superset** | Interactive dashboards and visual analytics |
| **Docker** | Containerization for consistent deployment |

---


## **Real-Time Analysis**

The pipeline enables **minute-level sales analysis** and real-time dashboards. Below is a sample visualization of sales over minutes:

<img width="100%" alt="Sales Analysis Dashboard" src="https://github.com/user-attachments/assets/8dba41f6-3bd6-49ba-a615-b98f0da0d247" />

---

## **Key Highlights**

- Fully containerized stack ensures **portability and reproducibility**.  
- Real-time streaming and processing pipeline with **low latency**.  
- Seamless integration of **Airflow, Kafka, Spark, Cassandra, and Superset**.  
- **Scalable architecture** suitable for large-scale streaming data.

---

