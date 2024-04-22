import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
from ingestion.dataWriter import DataProcessor

class ConfigLoader:
    def __init__(self, spark_session, path):
        self.spark = spark_session
        self.path = path
    
    def load_config(self):
        try:
            config_df = self.spark.read.json(self.path)
            config = config_df.collect()[0].asDict(recursive=True)
            return config
        except Exception as e:
            print(f"Failed to load configuration: {e}")
            raise

class DataProcessor:
    def __init__(self, spark, config):
        self.spark = spark
        self.config = config
    
    def read_data(self):
        try:
            df = self.spark.read.format(self.config["format"]).load(self.config["s3-path"])
            return df
        except Exception as e:
            print(f"Error reading data from {self.config['s3-path']}: {e}")
            raise
    
    def apply_schema(self, df):
        for field in self.config["schema"]:
            df = df.withColumn(field["name"], col(field["name"]).cast(field["type"]))
        return df
    
    def transform_data(self, df):
        for transform in self.config["transformations"]:
            if transform["type"] == "rename":
                df = df.withColumnRenamed("user_id", "uid")
        return df

    def handle_joins(self, df):
        for join in self.config.get("Joins", []):
            join_df = self.spark.table(join["table_name"])
            df = df.join(join_df, df["user_id"] == join_df["user_id"], how=join["type"])
        return df

    def add_columns(self, df):
        for add_col in self.config["add_columns"]:
            if "{PK}" in add_col["sql"]:
                pk_hash_expr = "+".join([f"cast({col} as string)" for col in self.config["PK"]])
                df = df.withColumn(add_col["col_name"], expr(f"hash({pk_hash_expr})"))
            else:
                df = df.withColumn(add_col["col_name"], expr(add_col["sql"].format(col_name=add_col["col_name"])))
        return df

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Dynamic Data Processing OOP") \
        .config('spark.jars.packages', 'com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.21.0') \
        .getOrCreate()
    config_path = "s3://your-config-bucket/config.json"

    try:
        config_loader = ConfigLoader(spark, config_path)
        config = config_loader.load_config()

        processor = DataProcessor(spark, config)
        df = processor.read_data()
        df = processor.apply_schema(df)
        df = processor.transform_data(df)
        df = processor.handle_joins(df)
        df = processor.add_columns(df)

        processor.write_to_bigquery(df)

    except Exception as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
