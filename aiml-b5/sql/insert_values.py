import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aiml",
    database="python_b5"
)
# mc = mydb.cursor()
# mc.execute('''insert into student
# values ("Raghu",101,25),
# ("Ravi",102,30),
# ("Raju",103,22);''')
# mydb.commit()
mc = mydb.cursor()
sql = '''insert into student values (%s,%s,%s);'''
val = [("Deepak",5,20),("Raghu",110,23)]
# mc.execute(sql,val)
mc.executemany(sql,val)
mydb.commit()