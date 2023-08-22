import sqlite3

conn = sqlite3.connect('bankData.db')
cur = conn.cursor()

print("Connection successful")

query1 = """
CREATE TABLE IF NOT EXISTS accounts (
    accountNo INT PRIMARY KEY,
    name VARCHAR,
    balance FLOAT,
    phoneNo INT,
    age INT
);
"""

cur.execute(query1)

print("Table created")

conn.close()

