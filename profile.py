import pandas as pd


# Load the raw dataset
df = pd.read_csv("chicago_crimes_raw.csv")


# Dataset Shape
print("\nDataset Shape:")
print(df.shape)


# Dataset Information
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html
print("\nData Type of Each Column:")
print(df.dtypes)


# Missing Values
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html
print("\nMissing Values:")
print(df.isna().sum())


# Duplicate Rows
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html
duplicate_rows = df.duplicated().sum()

print(
    f"\nDuplicate Rows: "
    f"{duplicate_rows}"
)


# Duplicate Record IDs
# The id field should uniquely identify each crime record
duplicate_ids = df["id"].duplicated().sum()

print(
    f"Duplicate IDs: "
    f"{duplicate_ids}"
)


# Key Analysis Fields
# Check the fields planned for the research question
analysis_columns = [
    "date",
    "primary_type",
    "district",
    "arrest"
]

print("\nMissing Values in Analysis Fields:")
print(
    df[analysis_columns]
    .isna()
    .sum()
)


# Crime Type Values
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html
print("\nCrime Type Counts:")
print(
    df["primary_type"]
    .value_counts()
)


# District Values
print("\nDistrict Counts:")
print(
    df["district"]
    .value_counts()
    .sort_index()
)


# Arrest Values
print("\nArrest Counts:")
print(
    df["arrest"]
    .value_counts()
    .sort_index())