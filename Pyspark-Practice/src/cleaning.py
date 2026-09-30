from pyspark.sql.functions import col

def clean_hr_data(df):
    # Remove unnecessary constant columns
    df = df.drop("Over18", "EmployeeCount", "StandardHours")

    # Rename MonthlyIncome
    df = df.withColumnRenamed(
        "MonthlyIncome", "Monthly_Income"
    )

    # Remove duplicate rows
    df = df.dropDuplicates()

    return df