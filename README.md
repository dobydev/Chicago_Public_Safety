# Chicago Crime and Arrest Outcome Analysis

This project analyzes reported crimes in Chicago to examine how crime type, police district, and time of occurrence are associated with the likelihood of an arrest.

The project was completed as part of the WGU M.S. Data Analytics - Data Engineering Capstone.

## Research Question

How do crime type, geographic location, and time of occurrence affect the likelihood of an arrest for reported crimes in Chicago?

## Project Overview

The project uses crime records from the City of Chicago Crimes - 2001 to Present dataset.

For this analysis, the dataset was limited to crimes reported during 2025. The data was collected directly from the City of Chicago Open Data API using Python.

The workflow includes:

1. Extracting crime data from the City of Chicago API
2. Profiling the raw dataset
3. Selecting and transforming the fields needed for analysis
4. Loading the transformed data into PostgreSQL
5. Performing descriptive analysis
6. Running a binary logistic regression
7. Interpreting arrest patterns by crime type, district, and time

## Data Source

City of Chicago  
Crimes - 2001 to Present

https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data

## Dataset

The extraction process retrieved:

- 238,110 crime records
- 22 original source fields
- Crimes occurring between January 1 and December 31, 2025

The API extraction used pagination in batches of up to 50,000 records and ordered results by the unique `id` field. :chatgpt-content-reference{index="0"}

## Project Structure

```text
chicago-public-safety-capstone/
│
├── extract.py
├── profile.py
├── transform.py
├── load.py
├── data_analysis.py
│
├── chicago_crimes_raw.csv
├── chicago_crimes_transformed.csv
├── logistic_regression_results.csv
│
└── README.md