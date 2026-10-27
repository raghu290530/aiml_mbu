import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aiml",
    database="python_b5"
)
def selectAll():
    mc = mydb.cursor()
    mc.execute('''select * from student;''')
    result = mc.fetchall()
    for e in result:
        print(e)
selectAll()