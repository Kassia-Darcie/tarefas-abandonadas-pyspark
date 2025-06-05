from pyspark.sql import SparkSession


def get_spark_session():
    return ( 
        SparkSession
        .builder
        .master("local[*]")
        .appName('spark_dataframe_api')
        .getOrCreate()
    )