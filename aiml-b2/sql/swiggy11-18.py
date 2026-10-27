import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="aiml",
    database = "aimlb2"
)
mc = mydb.cursor()
# List each student’s name alongside their city using JOIN. (Expected: 10 rows)

# mc.execute('''select s.name,a.city
# from students as s
# inner join addresses as a
# on s.roll_no=a.roll_no;''')
# r = mc.fetchall()
# for e in r:
#     print(e)

#Find the total marks obtained by each student
# (GROUP BY roll_no, ORDER BY total DESC).
# mc.execute('''select s.name,
# sum(m.marks_obtained) as total
#
# from students as s
# inner join marks as m
# on s.roll_no=m.roll_no
# group by s.name
# order by total desc;
# ''')
# r = mc.fetchall()
# for e in r:
#     print(e)

# 14-Count how many students are in each city.
# (Expected: Mumbai=3, Delhi=2, Pune=2)
def question14():
    mc.execute('''select a.city,count(s.roll_no)
    from students as s
    right join addresses as a
    on a.roll_no = s.roll_no
    group by a.city;
    ''')
    r = mc.fetchall()
    for e in r:
        print(e)
# question14()
# Find subjects where the average marks
# are below 50 (HAVING AVG < 50).
def question15():
    mc.execute('''select subject, avg(marks_obtained)
    from marks
    group by subject
    Having avg(marks_obtained)>50;
    ''')
    r = mc.fetchall()
    for e in r:
        print(e)
# question15()
def question18():
    mc.execute('''select s.name, m.subject,m.marks_obtained,
    case
        when m.marks_obtained>=80 then "A"
        when m.marks_obtained>=60 then "B"
        when m.marks_obtained>=40 then "C"
        else "D"
    end as grade
    from students as s
    inner join marks as m
    on m.roll_no = s.roll_no
    order by grade;
    ''')
    r = mc.fetchall()
    for e in r:
        print(e)
question18()