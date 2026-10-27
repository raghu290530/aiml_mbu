import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aiml",
    database = "student_managementb3"
)
mc = mydb.cursor()
#1 -
# mc.execute('''select s.name,a.city
# FROM students as s
# INNER JOIN addresses as a
# ON a.roll_no=s.roll_no;''')
# r = mc.fetchall()
# for e in r:
#     print(e)
#2-Find the total marks obtained by each
# student (GROUP BY roll_no, ORDER BY
# total DESC).

# mc.execute('''select s.name,sum(m.marks_obtained)
# FROM students as s
# INNER JOIN marks as m
# ON s.roll_no=m.roll_no
# GROUP BY m.roll_no
# ORDER BY sum(m.marks_obtained) desc;''')
# r = mc.fetchall()
# for e in r:
#     print(e)
#14 - Count how many students are in each city. (Expected: Mumbai=3, Delhi=2, Pune=2)
#15 - Find subjects where the average marks are below 50 (HAVING AVG < 50).
# mc.execute('''select subject, avg(marks_obtained) from marks
# group by subject
# having avg(marks_obtained)<50;''')
# r = mc.fetchall()
# for e in r:
#     print(e)

#16 List students who scored above 80 in any subject. (Expected: Aarav, Priya, Neha, Kavya)
mc.execute('''select distinct name
from students
inner join marks
on marks.roll_no=students.roll_no
where marks_obtained>80;''')
r = mc.fetchall()
for e in r:
    print(e)