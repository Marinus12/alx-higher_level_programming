#!/usr/bin/python3
"""Script takes in an argument and displays all values in the states table
hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE BINARY `name` =  \ 
    )
    [print(state) for state in c.fetchall()]
