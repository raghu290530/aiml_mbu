import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    # port=3307,
    password="aiml"
)
print(mydb)
mc = mydb.cursor()
mc.execute("show databases;")
r = mc.fetchall()
print(r)
for e in r:
    print(e)