
import mysql.connector
import pandas as pd
import numpy as np

data = pd.read_csv("E:\data analysts files dnld\sql\stock-data\data\Events_Announcements_Data.csv")
print(data)
def none_if_nan(value):
    if pd.isna(value) or value is np.nan:
        return None
    return value

def to_date_or_none(value):
    # Convert to pandas datetime or None if invalid
    try:
        dt = pd.to_datetime(value)
        return dt.date() if not pd.isna(dt) else None
    except:
        return None

# MySQL connection configuration - replace with your credentials
config = {
    'user': 'root',
    'password': '13412320013',
    'host': 'localhost',
    'database': 'stock_market'
}

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO company_events (symbol, company, purpose, event_date)
    VALUES (%s, %s, %s, %s)
   
    """

    for i, row in data.iterrows():
        print(f"Inserting {i+1} row")
        data_tuple = (
            none_if_nan(row['symbol']),
            none_if_nan(row['company']),
            none_if_nan(row['purpose']),
            to_date_or_none(row['event_date']),
        )
        cursor.execute(insert_query, data_tuple)

    connection.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
