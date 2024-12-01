#!/usr/bin/python3
"""
Lists all cities from the database that match the given state name.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    search = sys.argv[4]

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
        "SELECT cities.name FROM cities\
        JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id",
        [search]
    )
    query_rows = cur.fetchall()
    result = []
    for row in query_rows:
        result.append(row[0])

    print(", ".join(result))
    cur.close()
    conn.close()
