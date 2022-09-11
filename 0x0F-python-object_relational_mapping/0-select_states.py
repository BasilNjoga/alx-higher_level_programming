#!/usr/bin/python3
#This is a problem set on python 
db = MySQLdb.connect(host="localhost" user="root", passwd="", db ="hbtn_0e_0_usa")

cur = db.cursor()
c.execute("""SELECT * FROM states """)


