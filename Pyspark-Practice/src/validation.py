from pyspark.sql.functions import col

def validate_hr_data(df):
    # Check for null values
    null_counts = {
        column: df.filter(col(column).isNull()).count()
        for column in df.columns
    }

    # Check for duplicate rows
    total_rows = df.count()
    distinct_rows = df.dropDuplicates().count()
    duplicate_count = total_rows - distinct_rows

    # Display validation results
    print("Total rows:", total_rows)
    print("Duplicate rows:", duplicate_count)

    print("\nNull values:")
    for column, count in null_counts.items():
        if count > 0:
            print(column, ":", count)

    if all(count == 0 for count in null_counts.values()):
        print("No null values found.")

    return {
        "total_rows": total_rows,
        "duplicate_rows": duplicate_count,
        "null_counts": null_counts
    }