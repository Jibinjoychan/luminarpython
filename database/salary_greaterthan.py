import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="mysql",
    passwd="mysql",
    database="luminar")


cursor = db.cursor()

sql="""SELECT * FROM EMPLOYEEONE WHERE INCOME>18000"""
try:
    cursor.execute(sql)
    data=cursor.fetchall()
    print(data)
except Exception as e:
    print(e.args)

db.close()