import mysql.connector

def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        password="aiml",
        database = "aimlb2"
    )
    return mydb
# python -m pip install mysql-connector-python