from pyspark.sql.functions import col, when

def add_hr_features(df):
    # Convert attrition into a numeric flag
    df = df.withColumn(
        "Attrition_Flag",
        when(col("Attrition") == "Yes", 1).otherwise(0)
    )

    # Group employees by age
    df = df.withColumn(
        "Age_Group",
        when(col("Age") < 25, "Under 25")
        .when(col("Age") < 35, "25-34")
        .when(col("Age") < 45, "35-44")
        .when(col("Age") < 55, "45-54")
        .otherwise("55+")
    )

    return df