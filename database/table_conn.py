import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="mysql",
    passwd="mysql",
    database="luminar")

print(db)

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql="""CREATE TABLE EMPLOYEEONE(
       FIRST_NAME CHAR(20),
       LAST_NAME CHAR(20),
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT)"""
try:
    cursor.execute(sql)
except Exception as e:
    print(e.args)

db.close()