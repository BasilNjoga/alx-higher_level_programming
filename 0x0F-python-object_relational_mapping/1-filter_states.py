#!/usr/bin/python3
""" This is porblem set on mydsqdb """
import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)

cur = db.cursor()
cur.execute ("SELECT * FROM states ORDER BY states.id")
rows = cur.fetchall()
for row in rows:
	print(row)
cur.close()
db.close()

