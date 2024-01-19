#!/usr/bin/python3
"""
    This module filters states safely from the database
    hbtn_0e_0_usa with name starting with user input
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="{}".format(sys.argv[1]),
            passwd="{}".format(sys.argv[2]),
            db="{}".format(sys.argv[3]))

    cursor = db.cursor()
    cursor.execute("""
        SELECT
            id, name
        FROM
            states
        WHERE
            name = %(state)s
        ORDER BY
            states.id
        """, {'state': sys.argv[4]})

    rows = cursor.fetchall()
    for row in rows:
        print(row)
