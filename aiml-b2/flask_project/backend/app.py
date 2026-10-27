from flask import Flask, jsonify, request
import config

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Home Page"

@app.route("/mobiles")
def mobiles():
    return "Mobiles List"

@app.route("/mobiles/oppo")
def oppo_mobiles():
    return "Oppo Mobiles List"

@app.route("/students")
def students():
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute("select * from students;")
    r = mc.fetchall()
    return jsonify(r)

@app.route("/students/<int:id>",methods=["GET"])
def one_students(id):
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute('''select * from students where
    roll_no=%s;''',(id,))
    r = mc.fetchall()
    return jsonify(r)

@app.route("/students/<gender>",methods=["GET"])
def gender_students(gender):
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)
    mc.execute('''select * from students where
    gender=%s;''',(gender,))
    r = mc.fetchall()
    return jsonify(r)

@app.route("/stu",methods=["POST"])
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
    (%s,%s,%s,%s,%s);''',(roll_no,name,dob,gender,phone))
    mydb.commit()
    return "added new student"
@app.route("/stu/<int:id>",methods=["PUT"])
def modify_student(id):
    data = request.get_json()
    name = data["name"]
    mydb = config.connect()
    mc = mydb.cursor()
    mc.execute(''' update students
    set name=%s
    where roll_no=%s;''',(name,id))
    mydb.commit()
    return "added new student"

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
