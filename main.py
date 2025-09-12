import sqlite3

conn = sqlite3.connect("spinlog.db")
conn.execute("PRAGMA foreign_keys = ON;") # foreign key enforcement
cursor = conn.cursor()

# print tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables: ", cursor.fetchall())