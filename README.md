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


Technologies   
  
Apache Airflow    
Python    
Apache Kafka    
Apache Zookeeper    
Apache Spark 
Apache Superset
Cassandra    
PostgreSQL    
Docker          


**Below is the analysis we got for analysis sales data showing the sales over minutes**


<img width="1846" height="808" alt="Screenshot 2025-09-21 205628" src="https://github.com/user-attachments/assets/8dba41f6-3bd6-49ba-a615-b98f0da0d247" />







