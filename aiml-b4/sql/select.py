import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="aiml",
    database="mbu"
)
mc = mydb.cursor()
mc.execute("select * from student;")
r = mc.fetchall()
for e in r:
    print(*e)