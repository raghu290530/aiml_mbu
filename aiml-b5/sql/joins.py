import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aiml",
    database="student_management_b5"
)
def select_all():
    mc=mydb.cursor()
    # mc.execute('''select name,dob,city,state
    # from students
    # inner join addresses
    # on students.roll_no=addresses.roll_no;''')
    mc.execute('''select s.name,s.dob,a.city,a.state 
        from students as s
        inner join addresses as a
        on s.roll_no=a.roll_no;''')
    r = mc.fetchall()
    for e in r:
        print(e)
# select_all()

def question11():
    mc = mydb.cursor()
    mc.execute('''select s.name,a.city
    from students as s
    inner join addresses as a
    on s.roll_no=a.roll_no;''')
    r=mc.fetchall()
    for e in r:
        print(e)
# question11()
def question12():
    mc = mydb.cursor()
    mc.execute('''select s.name, 
    sum(m.marks_obtained) as total
    from students as s
    inner join marks as m
    on s.roll_no=m.roll_no
    group by s.name
    order by total desc;''')
    r=mc.fetchall()
    for e in r:
        print(e)
question12()