import sqlite3 as lite
import sys

def db_add(num, email):
    conn = lite.connect('numbers.db')
    cursor = conn.cursor()

    add = [num, email, 4]

    cursor.execute("INSERT INTO numbers (phone, email, sent) VALUES(?,?,?)", add)

    conn.commit()

    conn.close()


def db_getnums():
    conn = lite.connect('numbers.db')
    cursor = conn.cursor()
    nums = []

    cursor.execute("SELECT phone FROM numbers")

    for row in cursor.execute("SELECT phone FROM numbers"):
        nums.append(row[0])

    conn.close()
    return(nums)

def db_getfacts():
    conn = lite.connect('facts.db')
    cursor = conn.cursor()

    for row in cursor.execute("SELECT fact FROM facts ORDER BY RANDOM() LIMIT 1"):
        text = row[0]

    conn.close()

    return text

