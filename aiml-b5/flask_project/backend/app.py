from flask import Flask, jsonify, request
import config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome AIML B5"

@app.route("/products")
def all_products():
    return "Products List"

@app.route("/products/mobiles")
def all_mobiles():
    return "Mobiles List"

@app.route("/students")
def all_students():
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute('''select * from students;''')
    r = mc.fetchall()
    return jsonify(r)

@app.route("/addresses")
def all_addresses():
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute('''select * from addresses;''')
    r = mc.fetchall()
    return jsonify(r)

@app.route("/students/<int:id>")
def one_students(id):
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute('''select * from students
    where roll_no=%s;''',(id,))
    r = mc.fetchall()
    return jsonify(r)

@app.route("/students/<gender>", methods=["GET"])
def gender_students(gender):
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute('''select * from students
    where gender=%s;''',(gender,))
    r = mc.fetchall()
    return jsonify(r)

@app.route("/stu/",methods=["POST"])
def add_student():
    data = request.get_json()
    roll_no = data["roll_no"]
    name = data["name"]
    dob = data["dob"]
    gender = data["gender"]
    phone = data["phone"]
    mydb = config.connect()
    mc = mydb.cursor()
    mc.execute('''insert into students values
    (%s,%s,%s,%s,%s);''', (roll_no,name,dob,gender,phone))
    mydb.commit()
    return {"message": "Student added successfully"}

@app.route("/stu/<roll_no>", methods=["PUT"])
def update_student(roll_no):

    data = request.get_json()

    name = data["name"]
    dob = data["dob"]
    gender = data["gender"]
    phone = data["phone"]

    mydb = config.connect()
    mc = mydb.cursor()
    mc.execute("""
        UPDATE students
        SET name=%s, dob=%s, gender=%s, phone=%s
        WHERE roll_no=%s
    """, (name, dob, gender, phone, roll_no))

    mydb.commit()

    return {"message": "Student updated successfully"}
