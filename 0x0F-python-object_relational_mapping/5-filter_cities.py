#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT states.name, cities.name FROM cities\
                LEFT JOIN states ON state_id = states.id\
                where states.name LIKE %s\
                ORDER BY cities.id ASC;""", (argv[4],))
    cities1 = cur.fetchall()
    length = len(cities1)
    for i in range(length):
        if cities1[i][0] == argv[4]:
            cityy = str(cities1[i][1]).strip("(),'")
            if i < length - 1:
                print(cityy, end=', ')
            else:
                print(cityy)
    cur.close()
    conn.close()
