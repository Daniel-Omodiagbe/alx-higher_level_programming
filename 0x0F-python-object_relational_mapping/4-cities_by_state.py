#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities\
               INNER JOIN states ON state_id = states.id\
               ORDER BY cities.id ASC;""")
    cities1 = cur.fetchall()
    for city in cities1:
        print(city)
    cur.close()
    conn.close()
