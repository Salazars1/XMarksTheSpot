#!/usr/bin/python
import MySQLdb

#connect to database
db=MySQLdb.connect(host="localhost",user="xmarksthespot", passwd="xmarksthespot") 
# Create a Cursor object to execute queries.
cursor = db.cursor()
# delete database using SQL query.
cursor.execute("DROP DATABASE IF EXISTS DBXMarksTheSpot")
# Commit your changes in the database
db.commit()
# create database using SQL query.
f = open('DBcode.sql', 'r')
query = " ".join(f.readlines())
cursor.execute(query)
# disconnect from server
db.close()
