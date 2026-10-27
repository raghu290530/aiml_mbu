
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aiml",
    database = "swiggy_db"
)

mc = mydb.cursor()
sql = '''Select * from customers 
where city=%s or city=%s;'''
val = (input(),input())
mc.execute(sql,val)
result = mc.fetchall()
print(result)
for e in result:
    print(e)