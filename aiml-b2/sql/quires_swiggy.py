import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="aiml",
    database = "swiggy_db"
)

# mc = mydb.cursor()
# mc.execute('SELECT name,city FROM customers;')
# r = mc.fetchall()
# for x in r:
#   print(x)

#List all restaurants in 'Bangalore' sorted
# by rating descending. (Expected: Meghana Foods 4.5, Anand Bhavan 4.2, Chai Point 4.1)

mc = mydb.cursor()
mc.execute('''SELECT name,rating 
from restaurants
where city='Bangalore'
order by rating desc;''')
r = mc.fetchall()
for x in r:
  print(x)