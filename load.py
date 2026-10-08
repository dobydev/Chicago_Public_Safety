import pandas as pd

from db import conn  # Importing credentials from another file for security purposes

connection = conn


def load_data():
    print("Loading transformed CSV...")

    df = pd.read_csv("chicago_crimes_transformed.csv")

    print(f"Records to load: {len(df):,}")

    # Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.itertuples.html
    # Iterate over DataFrame rows as namedtuples
    records = list(
        df[[
            "id",
            "date",
            "primary_type",
            "district",
            "arrest",
            "hour",
            "day_of_week",
            "arrest_flag"
        ]].itertuples(index=False, name=None)
    )

    # Documentation: https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
    insert_query = """
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
    """

    # Open a cursor, insert all records, and close the connection
    with connection:
        with connection.cursor() as cursor:
            cursor.executemany(insert_query, records)

    connection.close()


load_data()