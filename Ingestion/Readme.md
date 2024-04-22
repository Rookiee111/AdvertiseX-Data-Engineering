The ingestion will happen via Spark. The spark code will be a generic one, instead of having one notebook per table, we will have generic spark code, that will be parametrised, such that it fetches the values from a config file. 
For explaining this better, following files have been added:
1) Config.json -> which is a sample config file, that explains the table load, 
