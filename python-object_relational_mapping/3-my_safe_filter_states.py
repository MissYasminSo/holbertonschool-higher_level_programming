#!/usr/bin/python3
"""Module: ORM module is going though how to use ORMs."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    cur = db.cursor()
    query = (
            "SELECT * "
            "FROM states "
            "WHERE name = %s "
            "ORDER BY id ASC"
            )
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    db.close()
