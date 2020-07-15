import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="mysql",
    passwd="mysql")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data=cursor.fetchone()
print("database version:",data)
db.close()
