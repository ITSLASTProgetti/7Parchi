#!/usr/bin /python

import sqlite3
conn = sqlite3.connect("./Parchi.db")
print("Opened database successfully");


try:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM [Parchi e giardini_Sona]')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as sqlerror:
    print("Error while connecting to sqlite", sqlerror)

.302.