#!/usr/bin/python3
"""  lists all states a name starting with N
    from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor_ = db.cursor()
    cursor_.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cursor_.fetchall()
    for row in rows:
        print(row)
    cursor_.close()
    db.close
