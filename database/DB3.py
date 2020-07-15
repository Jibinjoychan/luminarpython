import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="mysql",
    passwd="mysql",
    database="luminar")


cursor = db.cursor()

sql="""SELECT * FROM EMPLOYEEONE"""
try:
    cursor.execute(sql)
    data=cursor.fetchall() #fetchone used to print one person data
    print(data)
    #for value in data:
        #print(value)
except Exception as e:
    print(e.args)

db.close()