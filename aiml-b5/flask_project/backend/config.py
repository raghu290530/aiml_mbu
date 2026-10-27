import mysql.connector
def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user = "root",
        password="aiml",
        database = "student_management_b5 "
    )
    return mydb
