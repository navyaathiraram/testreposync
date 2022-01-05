from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

def helloFunction():
    print('bye')
    print(spark.conf.get("spark.databricks.service.clusterId"))
