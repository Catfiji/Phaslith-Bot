import mysql.connector

# connect to database
data = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='userdb'
)

# walk around in the database :O
cursor = data.cursor(dictionary=True)