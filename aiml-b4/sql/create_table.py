import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    port=3306,
    password="aiml",
    database="mbu"
)
mc = mydb.cursor()
# mc.execute('''create table student(
# id int, name varchar(50),age int);''')

#insert
# mc.execute('''insert into student values (
# 101,"Raghu",30)''')
# mydb.commit()
#
# #insert
# sql = "insert into student values (%s,%s,%s);"
# val = (102,"Ravi",25)
# mc.execute(sql,val)
# mydb.commit()

#insert MULIPLE
sql = "insert into student values (%s,%s,%s);"
val = [(102,"Ravi",25),(103,"Raju",20),(105,"Babu",20)]
mc.executemany(sql,val)
mydb.commit()
