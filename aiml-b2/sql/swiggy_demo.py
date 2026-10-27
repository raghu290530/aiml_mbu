import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password ="aiml",
    database = "swiggy_db"
)
# mc = mydb.cursor()

# mc.execute("CREATE DATABASE swiggy_db;")
# mc.execute("CREATE TABLE customers (customer_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL,city VARCHAR(50));")
# mc.execute('''CREATE TABLE restaurants (
#     restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     cuisine VARCHAR(50),
#     city VARCHAR(50),
#     rating DECIMAL(2,1)
# );''')

# sql = "INSERT INTO customers (name, city) VALUES (%s,%s);"
# val = [
#     ('Rahul Verma',  'Bangalore'),
#     ('Sneha Patel',  'Mumbai'),
#     ('Amit Singh',   'Delhi'),
#     ('Priya Nair',   'Bangalore'),
#     ('Vikash Kumar', 'Delhi'),
#     ('Meera Reddy',  'Hyderabad'),
#     ('Arjun Mehta',  'Mumbai'),
#     ('Deepa Iyer',   'Chennai')]
#
# mc.executemany(sql,val)
# mydb.commit()

mc = mydb.cursor()
mc.execute('SELECT name,city FROM customers;')

myresult = mc.fetchall()

for x in myresult:
  print(x)