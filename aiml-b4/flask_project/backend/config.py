import mysql.connector
# python -m pip install mysql-connector-python
def connect():
    mydb=mysql.connector.connect(
        host="localhost",
        user = "root",
        password="aiml",
        database="student_management_b4"
    )
    return mydb