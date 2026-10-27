from flask import Flask, jsonify, request
import config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Aiml B4"

@app.route("/products")
def all_products():
    mydb = config.connect()
    return "Connected"

@app.route("/products/mobile")
def all_mobiles():
    return "Mobiles list"

@app.route("/contact")
def contact():
    return "Contact us : 898955645"

@app.route("/students")
def all_students():
    mydb=config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute("select * from students;")
    r = mc.fetchall()
    return jsonify(r)
@app.route("/students/<int:id>",methods=["GET"])
def one_student(id):
    mydb=config.connect()
    mc = mydb.cursor(dictionary=True)
    sql='''select * from students 
    where roll_no=%s;'''
    val = (id,)
    mc.execute(sql,val)
    r = mc.fetchone()
    return jsonify(r)

@app.route("/stu/<gender>/<city>",methods=["GET"])
def city_student(gender,city):
    mydb=config.connect()
    mc = mydb.cursor(dictionary=True)
    sql='''select s.name,s.gender,a.city
     from students as s
     inner join addresses as a
     on s.roll_no=a.roll_no
     where s.gender=%s and a.city=%s;'''
    val = (gender,city)
    mc.execute(sql,val)
    r = mc.fetchall()
    return jsonify(r)

@app.route("/addresses")
def all_addresses():
    mydb=config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute("select * from addresses;")
    r = mc.fetchall()
    return jsonify(r)

@app.route("/addresses/<state>",methods=["GET"])
def all_city(state):
    mydb=config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute('''select * from addresses
    where state=%s''',(state,))
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

@app.route("/stu/<int:id>", methods=["DELETE"])
def delete_student(id):
    mydb = config.connect()
    mc = mydb.cursor()

    mc.execute("DELETE FROM students WHERE roll_no=%s", (id,))
    mydb.commit()

    if mc.rowcount == 0:
        return "Student not found", 404

    return "Student deleted successfully"