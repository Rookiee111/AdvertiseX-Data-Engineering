# AdvertiseX-Data-Engineering Case Study

![Design Image](Images/Design.png)

The overall design for this case study has been segmented into following sections:
1) Integration
2) Ingestion/ETL
3) Data Quality Framework
4) Data Warehouse

For the purpose of simplicity the following design has been based on a cloud platform, to be more specific AWS, however the technologies used are generic mostly can be leveraged and so the design can be implemented with other cloud platforms like Azure or GCP as well. 

Building a data platform expands to multiple persona's, which includes but not limited to:
- Data Analysts
- Data Modellers
- Data Engineers
- Data Scientists
- Product Managers/Scrum Master
- DevOps Engineer

Each play a critical role at different stages of the project. Me as a data engineer, plays a crucial role ensuring that the data is made available to the downstream consumers in timely manner, and in the state that the business/technical team can make sense of, after removing any noise which is needed. 

Phase 1:
**Integration**:
This piece is crucial as we build generic SDK (Ex: AWS Lambda + ECS) to bridge the gap between source and our landing zone. We essentially automate the process where our solution will bring in any new data from source and dump it into our landing cloud bucket (example: S3).
Here are the design consideration for this:
1) Create a solution that can be event driven app, which means, when ever source has new data, that should trigger AWS lambda to provision an ECS cluster to fetch data from source parallely and dump it into landing bucket.
2) Scheduled pipeline - Scheduled trigger for AWS lambda to trigger ECS that will do the copy from source to landing.

Error scenario:
If for whatever reason ECS fails or is not able to complete the copy of data, Lambda code should trigger a copy of data in landing folder to error archive in S3 such that the impartial data is not loaded, additionally log information should be recorded why ECS failed for which AWS's cloud logs can be helpful, which is a managed service. 

While this could be the case with Batch data loads, we need to have specialised app/sdk that can deal with real time data and ingest into kafka, so we can write our producers that can integrate with multiple real time sources and ingest the streams into Kafka. 

There are multiple error scenarios that needs to be considered, which not all are listed but some of them are:
1) How to make the producer resilient
2) How to deal with duplicates in case of failure

While these may not necessarily be scenarios that are handled at producer level, but its important to make these scalable as the volume of data could be high and cover off as much risk as possible.




