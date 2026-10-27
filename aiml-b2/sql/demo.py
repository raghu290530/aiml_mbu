import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    # host = "127.0.0.1",
    # port = 3306,
    user="root",
    password ="aiml"
)
print(mydb)
mc = mydb.cursor()
# mc.execute("create database raghu")
mc.execute("SHOW DATABASES")

for x in mc:
  print(x)