from logging import root

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="aiml"
)

if mydb:
    print("Connection Success")
else:
    print("Faild")

mc = mydb.cursor()

mc.execute("create database aimlb3_python;")
