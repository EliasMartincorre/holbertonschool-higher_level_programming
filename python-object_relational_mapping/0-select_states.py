#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa:
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connecting to a MySQL database
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Getting a Cursor in MySQL
    cur = db.cursor()

    # Executing MySQL Queries
    cur.execute('SELECT * FROM states ORDER BY id ASC')

    # Obtaining Query Results
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # Close all cursors jj
    cur.close()

    # Close all databases
    db.close()
