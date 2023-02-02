#WAP to create a table in mysql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fruit"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER(10), name VARCHAR(255), taste VARCHAR(255))")