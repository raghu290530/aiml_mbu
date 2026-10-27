import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="aiml"
)
print(mydb)

mc = mydb.cursor()
mc.execute("show databases;")
result = mc.fetchall()
print(result)
for e in result:
    print(e)