def load_hr_data(spark, file_path):
    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv("/Users/srishtikashyap/Desktop/Pyspark-Practice/Data/data.csv")
    )

    return df