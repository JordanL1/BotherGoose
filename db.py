import sqlite3 as lite

def db_add(num, email):

    """Add a number and an email address to the database.

    Keyword arguments:
    num -- phone number as a string
    email -- email address as a string
    """

    conn = lite.connect('numbers.db')
    cursor = conn.cursor()

    # "Sent" field was intended to track no. of messages sent, but we never implemented this
    add = [num, email, 4]

    cursor.execute("INSERT INTO numbers (phone, email, sent) VALUES(?,?,?)", add)

    conn.commit()

    conn.close()


def db_getnums():
    """Return a list of all numbers in the database."""
    conn = lite.connect('numbers.db')
    cursor = conn.cursor()
    nums = []

    cursor.execute("SELECT phone FROM numbers")

    for row in cursor.execute("SELECT phone FROM numbers"):
        nums.append(row[0])

    conn.close()
    return(nums)

def db_getfacts():
    """Return a random fact from the database."""
    conn = lite.connect('facts.db')
    cursor = conn.cursor()

    for row in cursor.execute("SELECT fact FROM facts ORDER BY RANDOM() LIMIT 1"):
        text = row[0]

    conn.close()

    return text

