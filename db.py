import sqlite3 as lite
import sys

def db_add(num, email):
    conn = lite.connect('numbers.db')
    cursor = conn.cursor()

    add = [num, email, 4]

    cursor.execute("INSERT INTO numbers (phone, email, sent) VALUES(?,?,?)", add)

    conn.commit()

    conn.close()


"""def db_getnums()
    conn = lite.connect('numbers.db')
    cursor = conn.cursor()

    cursor.execute("SELECT phone FROM numbers")

    for row in cursor.conn:
        nums = nums"""