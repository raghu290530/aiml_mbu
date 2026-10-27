import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aiml",
    database="student_management_b5"
)
def selcect_all():
    mc=mydb.cursor()
    mc.execute('''select * from students;''')
    r = mc.fetchall()
    for e in r:
        print(e)
# selcect_all()
def select_all_where():
    mc=mydb.cursor()
    sql = '''select * from students
     where roll_no>=%s;'''
    val = (5,)
    mc.execute(sql,val)
    r = mc.fetchall()
    for e in r:
        print(e)
select_all_where()