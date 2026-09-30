# IBM HR Analytics: Employee Attrition Analysis

## Project Overview

This project uses PySpark to analyze employee attrition in the IBM HR Analytics dataset. It demonstrates data loading, data cleaning, transformation, validation, and exploratory analysis.

## Technologies Used

* Python
* PySpark
* Pandas
* Matplotlib
* Jupyter Notebook
* Parquet

## Project Workflow

1. Load employee data from CSV.
2. Explore the dataset and understand its schema.
3. Check data quality, including missing values and duplicates.
4. Clean the data and remove unnecessary columns.
5. Create derived features such as age groups and attrition flags.
6. Perform employee attrition analysis using PySpark.
7. Visualize findings using Matplotlib.
8. Validate and save the processed data in Parquet format.

## Project Structure

```text
IBM-HR-PySpark-Project/
├── Data/
│   ├── data.csv
│   └── processed/
├── Notebooks/
│   ├── 01_exploration.ipynb
│   └── 06_business_insights.ipynb
└── src/
    ├── spark_session.py
    ├── data_loader.py
    ├── cleaning.py
    ├── transformations.py
    ├── validation.py
    └── pipeline.py
```

## Key Analysis

* Overall employee attrition
* Attrition by department, job role, and age group
* Relationship between overtime and attrition
* Impact of job satisfaction and tenure on attrition

## Dataset

IBM HR Analytics Employee Attrition & Performance dataset.

## How to Run

1. Install Python and Java.
2. Install PySpark and Jupyter.
3. Open the project in VS Code.
4. Run the notebooks in order.
5. Execute the pipeline to clean and transform the data.

## Disclaimer

This project uses a sample HR dataset for learning and demonstration. The observed relationships are descriptive and do not establish causation.



