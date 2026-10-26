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
            "SELECT cities.name "
            "FROM states "
            "INNER JOIN cities "
            "ON states.id=cities.state_id "
            "WHERE states.name = %s "
            "ORDER BY cities.id ASC"
            )
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    separator = ''
    for row in query_rows:
        print(separator, end='')
        print(row[0], end='')
        separator = ', '
    print()
    cur.close()
    db.close(
