#WAP to perform insert operation on a mysql database table.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="fruit"
)

mycursor = mydb.cursor()

sql = "INSERT INTO data (name, taste) VALUES (%s, %s)"
val = [
  ('Mango', 'Sweet'),
  ('Pineapple', 'Sour'),
  ('Orange', 'Sour'),
  ('Banana', 'Sweet'),
  ('Apple', 'Sweet')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")