import pandas as pd
import mysql.connector


data = pd.read_csv("E:/data analysts files dnld/sql/stock-data/data/Daily_Historical_Data.csv")
print(data)

# Step 3: Connect to MySQL
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='13412320013',
    database='stock_market'
)

cursor = connection.cursor()

# Insert data from DataFrame row-wise
insert_query = """
INSERT INTO stock_prices 
(symbol, trade_time, open_price, high_price, low_price, close_price, volume, intervals, trade_year)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

for i, row in data.iterrows():
    # Convert values accordingly if needed (e.g., to proper types)
    print(f"Inserting {i+1} row")
    data_tuple = (
        row['symbol'],
        row['trade_time'],
        float(row['open_price']),
        float(row['high_price']),
        float(row['low_price']),
        float(row['close_price']),
        int(row['volume']),
        row['intervals'],
        int(row['trade_year'])
    )
    cursor.execute(insert_query, data_tuple)

connection.commit()

# Step 7: Close connection
cursor.close()
connection.close()