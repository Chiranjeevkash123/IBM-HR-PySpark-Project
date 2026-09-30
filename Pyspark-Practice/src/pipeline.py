from data_loader import load_hr_data
from cleaning import clean_hr_data
from transformations import add_hr_features
from validation import validate_hr_data


def run_pipeline(spark, file_path):
    # Step 1: Load data
    df = load_hr_data(spark, file_path)

    # Step 2: Clean data
    cleaned_df = clean_hr_data(df)

    # Step 3: Add derived columns
    final_df = add_hr_features(cleaned_df)

    # Step 4: Validate data
    validation_results = validate_hr_data(final_df)

    return final_df, validation_results