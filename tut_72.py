# first install mysql-connector in cmd then code here

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Udoy", passwd="udoy436,", databases="udoy")

mycursor = mydb.cursor()

# mycursor.execute("show databases")
mycursor.execute("select * from teacher")

for i in mycursor:
    print(i)