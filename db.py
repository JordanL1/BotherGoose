import sqlite3 as lite
import sys

def db_add(num, email):
    conn = lite.connect('numbers.db')
    cursor = conn.cursor()
    id = cursor.lastrowid

    add = [id, num, email, 4]

    cursor.execute("INSERT INTO numbers VALUES(?,?,?,?)", add)

    print(cursor.fetchall())