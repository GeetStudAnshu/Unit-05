import mysql.connector

conn = mysql.connector.connect(
   user='root', 
   password='', 
   host='localhost', 
   database='fruit'
)
cursor = conn.cursor()
sql = '''SELECT * from data'''
cursor.execute(sql)
result = cursor.fetchall()
print(result)
conn.close()