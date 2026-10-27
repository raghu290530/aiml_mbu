import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aiml",
    database = "aimlb3_python"
)
print(mydb)

# mc = mydb.cursor()
# mc.execute('''create table student(
# id int, name varchar(50),age int);''')

# mc.execute("show tables;")
# for e in mc:
#     print(e)

mc = mydb.cursor()
sql = "insert into student values(%s,%s,%s);"
val = (101,"Raghu",25)
mc.execute(sql,val)
mydb.commit()