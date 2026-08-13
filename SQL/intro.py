"""
mysql-connector-python

"""
import mysql.connector

connector = mysql.connector.connect(
    host="localhost",            # server ip or host name
    user="root",                 # your mysql username
    password="root",             # your mysql password
    database="company_new"       # the specific database to use
)

if connector.is_connected():
    print("Database connected")

cursor = connector.cursor()
"""
cursor.execute("select * from employee")
rows = cursor.fetchall()
for i in rows:
    print(i)
"""
cursor.execute("select location,count(*) from employee group by location;")
rows = cursor.fetchall()
for i in rows:
    print(i)

cursor.close()
connector.close()