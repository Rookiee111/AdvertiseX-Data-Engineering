The ingestion will happen via Spark. The spark code will be a generic one, instead of having one notebook per table, we will have generic spark code, that will be parametrised, such that it fetches the values from a config file. 
For explaining this better, following files have been added:
1) Config.json -> which is a sample config file, it contains the configuration around which table to ingest data in, schema definition, transformations to perform, joins to perform and what metadata columns to add
2) genericDataLoader -> generic Spark code that reads the config and performs all the transformations as specific in config and writes it out.
3) genericConsumer -> its a spark streaming application that reads data from kafka, performs transformation.

The above code is just a psuedo code for demo and explainability purposes, and is not actually created/tested to be run. 
