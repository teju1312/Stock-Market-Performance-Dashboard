import mysql.connector
import pandas as pd
import numpy as np

data = pd.read_csv("E:/data analysts files dnld/sql/stock-data/data/Indices_data.csv")
print(data)
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
    INSERT INTO index_data
    (index_category, `index`, symbol, open, high, low, prev_close, ltp, indicative_close,
     chng, percent_chng, volume_shares, value_crores, high_52w, low_52w, percent_chng_30d, percent_chng_365d)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    open = VALUES(open), high = VALUES(high), low = VALUES(low), prev_close = VALUES(prev_close),
    ltp = VALUES(ltp), indicative_close = VALUES(indicative_close), chng = VALUES(chng),
    percent_chng = VALUES(percent_chng), volume_shares = VALUES(volume_shares),
    value_crores = VALUES(value_crores), high_52w = VALUES(high_52w), low_52w = VALUES(low_52w),
    percent_chng_30d = VALUES(percent_chng_30d), percent_chng_365d = VALUES(percent_chng_365d)
    """

    for i, row in data.iterrows():
        print(f"Inserting {i+1} row")
        data_tuple = (
            none_if_nan(row['index_category']),
            none_if_nan(row['index']),
            none_if_nan(row['symbol']),
            to_float_or_none(none_if_nan(row['open'])),
            to_float_or_none(none_if_nan(row['high'])),
            to_float_or_none(none_if_nan(row['low'])),
            to_float_or_none(none_if_nan(row['prev_close'])),
            to_float_or_none(none_if_nan(row['ltp'])),
            to_float_or_none(none_if_nan(row['indicative_close'])),
            to_float_or_none(none_if_nan(row['chng'])),
            to_float_or_none(none_if_nan(row['percent_chng'])),
            to_int_or_none(none_if_nan(row['volume_shares'])),
            to_float_or_none(none_if_nan(row['value_crores'])),
            to_float_or_none(none_if_nan(row['high_52w'])),
            to_float_or_none(none_if_nan(row['low_52w'])),
            to_float_or_none(none_if_nan(row['percent_chng_30d'])),
            to_float_or_none(none_if_nan(row['percent_chng_365d'])),
        )
        cursor.execute(insert_query, data_tuple)

    connection.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
