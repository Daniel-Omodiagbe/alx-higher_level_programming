#!/usr/bin/python3
"""lists all values in a state"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name = '{:s}'\
     ORDER BY states.id ASC""".format(argv[4]))
    states1 = cur.fetchall()
    for state in states1:
        if state[1] == argv[4]:
            print(state)
    cur.close()
    conn.close()
