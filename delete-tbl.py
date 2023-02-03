import mysql.connector

conn = mysql.connector.connect(
   user='root', 
   password='', 
   host='localhost', 
   database='fruit'
)

cursor = conn.cursor()

print("Contents of the table: ")
cursor.execute("SELECT * from data")
print(cursor.fetchall())

sql = "DELETE FROM data WHERE id > '%d'" % (3)

try:
   cursor.execute(sql)
   conn.commit()
except:
   conn.rollback()

print("Contents of the table after delete operation ")
cursor.execute("SELECT * from data")
print(cursor.fetchall())

conn.close()