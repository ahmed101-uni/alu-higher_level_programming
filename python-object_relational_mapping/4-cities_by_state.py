#!/usr/bin/python3
"""
Script that connects to a MySQL database, retrieves all rows from
the 'cities' table, and prints them in ascending order by 'id'.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbName,
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
         JOIN states ON cities.state_id = states.id"
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
