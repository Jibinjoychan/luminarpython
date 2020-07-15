import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="mysql",
    passwd="mysql",
    database="luminar")

print(db)

cursor = db.cursor()

sql="""INSERT INTO EMPLOYEEONE(
       FIRST_NAME,
       LAST_NAME,
       AGE,
       SEX,
       INCOME) VALUES('ALFA','J',22,'F',13000)"""
try:
    cursor.execute(sql)
    db.commit()       #commit used for save changes
except Exception as e:
    db.rollback() #exception occur cheyta value store akila
    print(e.args)
    
finally:
db.close()