import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aiml",
    database="python_b5"
)
mc = mydb.cursor()
# mc.execute("create database python_b5;")
mc.execute('''create table student(
name varchar(50),id int,age int);''')