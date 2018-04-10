#!/usr/bin/python
import MySQLdb
from datetime import date
import calendar

my_date = date.today()
reset_day_occuring = calendar.day_name[my_date.weekday()]
day_to_reset = ""
if(reset_day_occuring == 'Monday'):
    day_to_reset = 'Sunday'
if(reset_day_occuring == 'Tuesday'):
    day_to_reset = 'Monday'
if(reset_day_occuring == 'Wednesday'):
    day_to_reset = 'Tuesday'
if(reset_day_occuring == 'Thursday'):
    day_to_reset = 'Wednesday'
if(reset_day_occuring == 'Friday'):
    day_to_reset = 'Thursday'
if(reset_day_occuring == 'Saturday'):
    day_to_reset = 'Friday'
if(reset_day_occuring == 'Sunday'):
    day_to_reset = 'Saturday'

#print(reset_day_occuring)
#print(day_to_reset)
#connect to database
db=MySQLdb.connect(host="localhost",user="root", passwd="2016x", db="DBXMarksTheSpot")
# Create a Cursor object to execute queries.
cursor = db.cursor()

# delete from table buildings_reservation where day has a certain date command
cursor.execute("DELETE FROM buildings_reservation WHERE day = %s", (day_to_reset,) )
# Commit your changes in the database
db.commit()

# disconnect from server
db.close()
