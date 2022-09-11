#!/usr/bin/python3
#This is a problem set on python 
import MySQLdb
db = MySQLdb.connect(passwd="root", db ="hbtn_0e_0_usa")

cur = db.cursor()
cur.execute("""SELECT * FROM states """)


