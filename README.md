# AdvertiseX-Data-Engineering Case Study

![Design Image](Images/Design.png)

The overall design for this case study has been segmented into following sections:
1) Integration
2) Ingestion/ETL
3) Data Quality Framework
4) Data Warehouse

The case study is for adtech firm AdvertiseX, it help its partners with digital ad campaigns and tracking market penetration using such adverts. The data associated from such company is of diverse in nature, it contains datasets such as ad clicks data, demographic data of users showing interest in advertisement, location data etc. The design of the platform is performed considering the nature of data and the volume of it. 

**Tech stack**
The architecture of this platform is designed to leverage cloud technologies that offer dependable services with the promise of high availability, reliability, and reduced maintenance overhead. The cloud strategy in this design incorporates a hybrid approach utilizing both AWS and GCP, selected for their mature and continuously improving offerings. These providers have demonstrated robust and reliable technology stacks through years of operation and iterative enhancements. But with that said, the tech I have opted for can be deployed with other cloud offerings as well, however, how reliable those tech's are is something that will have to be checked. 

The overall architecture is divided into multiple phases
1) **Integration**
2) **Ingestion**
3) **Data Quality**
4) **Data Warehouse**

**Integration**:
To source data from various origins, I have opted for AWS Lambda, ECS, and EC2 instances. These services are cost-effective, support event-driven or scheduled operations, and allow for dynamic computational optimization of data movement applications. Furthermore, they facilitate logging within cloud services, which substantially aids in reducing the time needed for issue resolution from a support perspective.

**Storage**
For a storage solution that is scalable and format-agnostic, I have selected Amazon S3. It is inherently scalable, fault-tolerant, cost-effective, and offers flexible management features for user access. Furthermore, S3 includes lifecycle management policies that can help in reducing costs by automating the deletion or migration of data.

**Compute For Ingestion**
For the pub/sub system, I've chosen Apache Kafka for several compelling reasons:
1) Kafka is inherently distributed, enabling high-throughput data handling by accommodating multiple producers and consumers simultaneously.
2) It ensures fault tolerance through internal replication of topics, safeguarding against data loss.
3) Kafka is a well-established technology that has undergone significant enhancements, such as the ability to perform in-stream data transformations, reducing the latency typically introduced by auxiliary services (unlike systems like Kinesis Data Streams).
4) Kafka offers both managed services and serverless options to cater to a range of deployment preferences.

For data processing, I've selected Apache Spark for its versatility:

1) Apache Spark is a comprehensive engine that accommodates batch processing, real-time processing, and machine learning tasks.
2) As a distributed system, Spark processes data in parallel, showcasing resilience, fault tolerance, and employing lazy evaluation — it commences processing only upon an action call, which is more efficient than traditional MapReduce.
3) Spark can be accessed as a SaaS, like Databricks, offering additional features for ease of use and eliminating the complexity of cluster configuration and maintenance.
4) Its a matured tech with integration with various source/sinks

**Data Quality**
Data quality is a pivotal element of any data platform, necessitating robust rules for data validation. While some rules can preemptively filter out erroneous data during processing, others may need to be defined by business users or data analysts. The specific service for implementing these rules remains undefined in the design to allow flexibility based on requirements and cost considerations. Options range from open-source Python libraries, which support config-based rules for data ingestion quality checks, to comprehensive paid solutions like Collibra that offer advanced features and support, contributing to a future-proof and reliable system. The choice ultimately hinges on the specific needs and budget constraints.

For **data anomaly detection**, employing a machine learning model trained on high-quality labeled data is essential. Clustering algorithms are a practical choice for identifying and weeding out outliers. The threshold for anomalies typically aligns with business standards; a 95% threshold is often regarded as high quality. However, thresholds can vary based on the trade-off between data pipeline integrity and the permissible impact on data quality. In some projects I've managed, an 80% threshold balanced this consideration, allowing for a certain degree of leniency in the data pipeline while maintaining acceptable data quality standards.

**Data Warehouse**
For this my choice is BigQuery,for multiple reasons:
1) It is serverless, eliminating the need for cluster management overhead.
2) BigQuery is highly scalable and adept at handling large volumes of data.
3) It supports geospatial analysis, which is pertinent to this project's requirements.
4) The cost-effectiveness of BigQuery is appealing, especially given its capabilities.
5) BigQuery integrates seamlessly with BI tools, enabling efficient data retrieval for dashboarding—a task that can challenge other services like Redshift, which may experience performance degradation under similar workloads.
6) It offers comprehensive access control features, allowing for granular management of user permissions.

**Optional**
AWS Athena is an excellent choice for data exploration because it allows users like product managers and data scientists to directly access raw data without the need for time-consuming preparation and ingestion into tables by data engineers. 
Built on the Presto distributed SQL query engine, Athena enables querying data directly from S3 in a structured format, facilitating swift data exploration. This can significantly shorten the time to market decision-making. 
Athena is not only cost-effective and user-friendly with its support for SQL but also boasts fast performance. It's engineered on principles similar to Spark and integrates seamlessly with other AWS services.

**Orchestration**
Apache Airflow is a robust choice for orchestrating complex data workflows, thanks to its open-source nature, which makes it a cost-effective solution. 
1) Airflow provides exceptional flexibility for developing custom pipelines, with extensive options for interfacing with diverse data sources and destinations. 
2) It's built with a rich set of APIs that facilitate not only scheduling but also event-driven execution of tasks. 
3) Technically, Airflow's design, based on directed acyclic graphs (DAGs), allows for clear and manageable structuring of data tasks, which simplifies dependencies and scheduling. 
4) The dynamic pipeline generation feature enables creating workflows that are dynamic and responsive to changes in data or environment. 
5) Additionally, Airflow’s rich user interface provides detailed visibility into the status of tasks, logs, and troubleshooting – a valuable feature for monitoring pipeline health and failure recovery.
6) With a large and active community, users benefit from a vast repository of custom operators and frequent updates, further enhancing its capabilities and resilience.


 
















