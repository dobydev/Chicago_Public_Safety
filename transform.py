import pandas as pd


# Load the raw dataset
df = pd.read_csv("chicago_crimes_raw.csv")


# Select Analysis Fields
analysis_columns = [
    "id",
    "date",
    "primary_type",
    "district",
    "arrest"
]

df = df[analysis_columns].copy()


# Date Transformation
# Convert the incident date from text to datetime
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
df["date"] = pd.to_datetime(df["date"])


# Time Features
# Extract the hour from the incident date
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.hour.html
df["hour"] = df["date"].dt.hour

# Extract the day of the week from the incident date
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html
df["day_of_week"] = df["date"].dt.day_name()


# Geographic Variable
# Convert district to text because it represents a category
# rather than a continuous numeric value
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html
df["district"] = df["district"].astype(str)


# Categorical Encoding
print("\nArrest Values Before Encoding:")
print(
    df["arrest"]
    .value_counts()
    .sort_index()
)

# Encode arrest as 0 for no arrest and 1 for arrest
df["arrest_flag"] = df["arrest"].astype(int)

print(
    "\nCategorical Encoding: arrest was encoded as "
    "0 for no arrest and 1 for arrest."
)

print("\nArrest Values After Encoding:")
print(
    df["arrest_flag"]
    .value_counts()
    .sort_index()
)


# Final Verification
print("\nTransformed Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isna().sum())

print("\nData Types:")
print(df.dtypes)

print("\nTransformed Dataset Preview:")
print(df.head())


# Save the transformed dataset
# Documentation:
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
df.to_csv(
    "chicago_crimes_transformed.csv",
    index=False
)

print("\nTransformed dataset saved successfully.")