class DataProcessor:
    def __init__(self, spark, config):
        self.spark = spark
        self.config = config

    # Existing methods unchanged...

    def write_to_bigquery(self, df):
        self.spark.conf.set('temporaryGcsBucket', self.config["temp_gcs_bucket"])

        # Write DataFrame to BigQuery
        df.write.format('bigquery') \
            .option('table', self.config["bigquery_table"]) \
            .option('temporaryGcsBucket', self.config["temp_gcs_bucket"]) \
            .mode('append') \
            .save()
