#  mysql.connector: Used to connect to and interact with the MySQL database.
#  pandas: Used for handling CSV data in a structured DataFrame.
#  numpy: Used to handle NaN values and numeric operations.
import mysql.connector
import pandas as pd
import numpy as np

# Load CSV and strip whitespace
data = pd.read_csv("E:\\data analysts files dnld\\sql\\stock-data\\data\\Stock_Details_Data.csv")
data.columns = data.columns.str.strip()

# Convert date columns to datetime
# errors='coerce' converts invalid/missing dates to NaT (treated as null).
data['date_of_listing'] = pd.to_datetime(data['date_of_listing'], errors='coerce')
data['load_date'] = pd.to_datetime(data['load_date'], errors='coerce')

# The function none_if_nan checks if a value is NaN-Not A Number (from pandas or NumPy), and if so, 
# it converts it to None. Otherwise, it returns the original value.
# isna() function is used to detect missing values 
# True indicates the presence of a missing value (like NaN, None, or pd.NA). & false means value is valid.
def none_if_nan(value):
    if pd.isna(value) or value is np.nan:
        return None
    return value

def to_float_or_none(value):
    if value is None:
        return None
    return float(value)

def to_int_or_none(value):
    if value is None:
        return None
    return int(value)

config = {
    'user': 'root',
    'password': '13412320013',
    'host': 'localhost',
    'database': 'stock_market'
}

# Creates a cursor to perform database operations.
try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
# Inserts a new row or updates the existing row if a duplicate key (symbol and token) is found.
    insert_query = """
    INSERT INTO stock_master
    (symbol, token, intraday_margin, name, date_of_listing, lot, paid_up_value, isin,
     face_value, bse_group, sector, industry, industry_new, igroup, isubgroup, load_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
     intraday_margin = VALUES(intraday_margin),
     name = VALUES(name),
     date_of_listing = VALUES(date_of_listing),
     lot = VALUES(lot),
     paid_up_value = VALUES(paid_up_value),
     isin = VALUES(isin),
     face_value = VALUES(face_value),
     bse_group = VALUES(bse_group),
     sector = VALUES(sector),
     industry = VALUES(industry),
     industry_new = VALUES(industry_new),
     igroup = VALUES(igroup),
     isubgroup = VALUES(isubgroup),
     load_date = VALUES(load_date);
    """

# Constructs a tuple data_tuple with the row's values after converting NaNs to None and casting to proper types.
    for i, row in data.iterrows():
        data_tuple = (
            none_if_nan(row['symbol']),
            to_int_or_none(none_if_nan(row['token'])),
            to_float_or_none(none_if_nan(row['intraday_margin'])),
            none_if_nan(row['name']),
            none_if_nan(row['date_of_listing']),
            to_float_or_none(none_if_nan(row['lot'])),
            to_float_or_none(none_if_nan(row['paid_up_value'])),
            none_if_nan(row['isin']),
            to_float_or_none(none_if_nan(row['face_value'])),
            none_if_nan(row['bse_group']),
            none_if_nan(row['sector']),
            none_if_nan(row['industry']),
            none_if_nan(row['industry_new']),
            none_if_nan(row['igroup']),
            none_if_nan(row['isubgroup']),
            none_if_nan(row['load_date']),
        )
        print(f"Inserting row {i+1}: {data_tuple}")  # Debug: Data sent to MySQL
        cursor.execute(insert_query, data_tuple)

    connection.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()



# Summary
# This script reads a CSV into a pandas DataFrame, cleans and converts data,
#  then inserts or updates rows in a MySQL table row-by-row, 
# handling NULLs carefully with helper functions and printing debug information for each row inserted.