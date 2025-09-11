import sqlite3

conn = sqlite3.connect("spinlog.db")
cursor = conn.cursor()

with open("schema.sql", "r") as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()
print("Database created with schema!")
