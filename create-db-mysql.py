# Create DB
import mysql.connector
db = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd =""
)
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS fruit")