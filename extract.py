import requests
import pandas as pd


API_URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
rows = []


# Documentation:
# https://docs.python.org/3.12/library/stdtypes.html#range
def extract_chicago_crime_data():
    for offset in range(0, 250000, 50000):

        # Adopted from:
        # https://support.socrata.com/hc/en-us/articles/202949268-How-to-query-more-than-1000-rows-of-a-dataset
        response = requests.get(
            API_URL,
                params={
                    "$limit": 50000,
                    "$offset": offset,
                    "$where": (
                    "date >= '2025-01-01T00:00:00' "
                    "AND date < '2026-01-01T00:00:00'"),
                    "$order": "id",
                },
            timeout=120
        )

        # Check that the request is successful
        # https://docs.python-requests.org/en/latest/user/quickstart/#json-response-content
        response.raise_for_status()

        batch = response.json()

        # Add records to the rows list
        rows.extend(batch)

        # Keep track of rows being extracted
        print(f"Downloaded {len(rows):,} rows")
        
extract_chicago_crime_data()

# Turn the rows list into a DataFrame
df = pd.DataFrame(rows)

print(df.shape)
print(df.head())

# Save raw API data locally
df.to_csv("chicago_crimes_raw.csv", index=False)

print("Raw dataset saved successfully.")







