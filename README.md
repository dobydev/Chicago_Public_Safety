# Chicago Public Safety ETL Pipeline

This project is a Python-based ETL pipeline built using the City of Chicago Crimes - 2001 to Present dataset.

The pipeline extracts Chicago crime records from the City of Chicago Open Data API, profiles and validates the raw data, transforms the fields needed for downstream use, and loads the prepared records into PostgreSQL.

The project focuses on core data engineering concepts such as API ingestion, data profiling, transformation, relational database loading, and data-quality validation.

---

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
     create_table.sql
            |
            v
         load.py
            |
            v
       PostgreSQL
```

---

## Data Source

**City of Chicago - Crimes 2001 to Present**

https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data

The pipeline is configured to retrieve crime records occurring during calendar year 2025.

A total of **238,110 records** were extracted and processed.

---

## Repository Structure

```text
chicago-public-safety-capstone/
│
├── README.md
├── create_table.sql
├── extract.py
├── load.py
├── profile.py
└── transform.py
```

Generated CSV files and database credentials are not stored in this repository

---

## Extract

`extract.py` retrieves crime records directly from the City of Chicago Open Data API.

The extraction process uses Socrata query parameters to manage a large API response:

- `$where` filters records to 2025
- `$limit` retrieves up to 50,000 records per request
- `$offset` moves through the dataset in batches
- `$order=id` keeps records in a consistent order

The script combines each API response into a single Pandas DataFrame and saves the unmodified result as:

```text
chicago_crimes_raw.csv
```

The raw file is preserved before transformation so the original extracted data remains available if the pipeline needs to be rerun or validated.

### Run

```bash
python extract.py
```

---

## Profile

`profile.py` performs data-quality checks on the raw dataset before transformation.

The profiling process checks:

- Dataset dimensions
- Column data types
- Missing values
- Duplicate rows
- Duplicate record IDs
- Crime type counts
- Police district counts
- Arrest counts

The script also verifies the completeness of the fields required by the transformation process:

```text
date
primary_type
district
arrest
```

This step helps identify data-quality problems before changes are made to the raw data.

### Run

```bash
python profile.py
```

---

## Transform

`transform.py` prepares the raw data for structured database storage.

The transformation process:

- Selects the required source fields
- Converts the incident date into a datetime value
- Derives the hour of occurrence
- Derives the day of the week
- Converts police district to a categorical text field
- Encodes arrest status into a binary field
- Validates the transformed dataset
- Saves the transformed output to a separate CSV

The final schema contains:

```text
id
date
primary_type
district
arrest
hour
day_of_week
arrest_flag
```

The `arrest_flag` field is encoded as:

```text
0 = No Arrest
1 = Arrest
```

The transformed dataset is saved as:

```text
chicago_crimes_transformed.csv
```

### Run

```bash
python transform.py
```

---

## PostgreSQL Schema

`create_table.sql` creates the destination PostgreSQL table used by the load process.

```sql
CREATE TABLE IF NOT EXISTS chicago_crimes (
    id BIGINT PRIMARY KEY,
    date TIMESTAMP,
    primary_type VARCHAR(150),
    district VARCHAR(10),
    arrest BOOLEAN NOT NULL,
    hour INTEGER,
    day_of_week VARCHAR(50),
    arrest_flag INTEGER NOT NULL CHECK (arrest_flag IN (0, 1))
);
```

The schema includes:

- A primary key on `id`
- Data types matching the transformed dataset
- A check constraint ensuring `arrest_flag` contains only `0` or `1`

Run this SQL in PostgreSQL before executing the load script.

---

## Load

`load.py` loads `chicago_crimes_transformed.csv` into PostgreSQL.

The script:

- Reads the transformed CSV with Pandas
- Converts DataFrame records into tuples
- Uses a parameterized SQL `INSERT`
- Inserts the transformed records into `chicago_crimes`
- Uses `ON CONFLICT (id) DO NOTHING` to prevent duplicate primary-key inserts

The insert operation uses:

```sql
INSERT INTO chicago_crimes (
    id,
    date,
    primary_type,
    district,
    arrest,
    hour,
    day_of_week,
    arrest_flag
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (id) DO NOTHING;
```

### Run

```bash
python load.py
```

The completed load contains:

```text
238,110 records
```

---

## Database Connection

`load.py` imports the PostgreSQL connection from a local `db.py` file.

Example local configuration:

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="chicago_crimes",
    user="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    port="5432"
)
```

Add `db.py` to `.gitignore`:

```gitignore
db.py
.venv/
__pycache__/
*.pyc
```

---

## Data Validation

The pipeline includes validation throughout the ETL process.

Examples include:

- API response status validation
- Running extraction record counts
- Missing-value checks
- Duplicate-row checks
- Duplicate-ID checks
- Data type verification
- Final transformed-dataset validation
- PostgreSQL primary-key enforcement
- Binary-value constraint enforcement
- Database row-count verification

The final PostgreSQL record count was validated against the transformed dataset:

```sql
SELECT COUNT(*)
FROM chicago_crimes;
```

Expected result:

```text
238110
```

---

## Technologies

- Python
- Pandas
- Requests
- PostgreSQL
- psycopg2
- SQL
- Socrata Open Data API

---

## Python Dependencies

Install the required Python packages:

```bash
pip install pandas requests psycopg2-binary
```

---

## Running the Pipeline

Run the project in the following order:

```bash
python extract.py
python profile.py
python transform.py
```

Create the PostgreSQL table using:

```text
create_table.sql
```

Then load the transformed data:

```bash
python load.py
```

---

## Pipeline Outputs

### Raw Dataset

```text
chicago_crimes_raw.csv
```

Contains the combined API response before transformation.

### Transformed Dataset

```text
chicago_crimes_transformed.csv
```

Contains the prepared records matching the PostgreSQL destination schema.

### PostgreSQL Table

```text
chicago_crimes
```

Contains the final structured records produced by the ETL pipeline.

---

## Data Engineering Concepts Demonstrated

This project demonstrates:

- REST API ingestion
- API pagination
- Filtered source extraction
- Batch processing
- Raw data preservation
- Data profiling
- Missing-value validation
- Duplicate detection
- Schema selection
- Data type conversion
- Derived fields
- Categorical encoding
- CSV staging
- Relational schema design
- Parameterized SQL inserts
- Primary-key enforcement
- Database constraints
- Duplicate-safe loading
- End-to-end ETL validation

---

## Future Improvements

Possible engineering improvements include:

- Replacing row inserts with PostgreSQL `COPY` for faster bulk loading
- Moving database configuration to environment variables
- Adding structured logging
- Adding automated data-quality tests
- Containerizing the pipeline with Docker
- Scheduling the pipeline with an orchestration tool such as Apache Airflow
- Loading incremental records instead of performing full-year extracts

---

## Author

**Gabriel Doby**

Data Engineering Capstone Project  
Western Governors University
