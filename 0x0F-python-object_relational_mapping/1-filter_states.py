#!/usr/bin/python3
"""lists all states from the database starting with N"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N'\
     ORDER BY states.id ASC")
    states1 = cur.fetchall()
    for state in states1:
        if state[1][0] == "N":
            print(state)
    cur.close()
    conn.close()
