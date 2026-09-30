from pyspark.sql import SparkSession

def create_spark_session():
    spark = (
        SparkSession.builder
        .appName("IBM_HR_Analytics_Project")
        .getOrCreate()
    )

    return spark
