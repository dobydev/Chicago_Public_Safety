# Chicago Public Safety ETL Pipeline

This project is a data engineering pipeline built around the City of Chicago Crimes - 2001 to Present dataset.

The pipeline extracts 2025 Chicago crime records from the City of Chicago Open Data API, profiles and validates the raw data, transforms the fields needed for downstream use, and loads the prepared dataset into PostgreSQL.

## Project Overview

The ETL workflow follows four main stages:

1. Extract crime records from the City of Chicago API
2. Profile and validate the raw dataset
3. Transform the data into an analysis-ready structure
4. Load the transformed records into PostgreSQL

The pipeline processed 238,110 crime records from 2025.

## Data Source

City of Chicago  
Crimes - 2001 to Present

https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data

## ETL Workflow

```text
City of Chicago Open Data API
            |
            v
        extract.py
            |
            v
 chicago_crimes_raw.csv
            |
            v
        profile.py
            |
            v
       transform.py
            |
            v
chicago_crimes_transformed.csv
            |
            v
         load.py
            |
            v
       PostgreSQL