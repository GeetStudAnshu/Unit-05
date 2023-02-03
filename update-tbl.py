import mysql.connector

conn = mysql.connector.connect(
   user='root', 
   password='', 
   host='localhost', 
   database='fruit'
)

cursor = conn.cursor()

sql = '''UPDATE data SET name="Watermelon" WHERE id = 5 '''
try:
   cursor.execute(sql)
   conn.commit()
except:
   conn.rollback()

sql = 'SELECT * from data'
cursor.execute(sql)
print(cursor.fetchall())

conn.close()