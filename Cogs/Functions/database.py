import mysql.connector

data = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='userdb'
)

cursor = data.cursor(dictionary=True)