
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
import config

app = Flask(__name__)

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


# HOME PAGE: /
@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


# STUDENT LIST PAGE: /students
@app.route("/students")
def students_page():
    return send_from_directory(FRONTEND_DIR, "index.html")


# FULL STUDENT DETAILS PAGE: /students/1
@app.route("/students/<int:id>")
def student_details_page(id):
    return send_from_directory(FRONTEND_DIR, "index.html")


# API: GET ALL STUDENTS
@app.route("/api/students", methods=["GET"])
def get_students():
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)

    try:
        mc.execute("""
            SELECT roll_no, name, dob, gender, phone
            FROM students
            ORDER BY roll_no
        """)

        students = mc.fetchall()

        for student in students:
            if student["dob"]:
                student["dob"] = student["dob"].isoformat()

        return jsonify(students)

    finally:
        mc.close()
        mydb.close()


# API: GET ONE STUDENT
@app.route("/api/students/<int:id>", methods=["GET"])
def get_student(id):
    mydb = config.connect()
    mc = mydb.cursor(dictionary=True)

    try:
        mc.execute("""
            SELECT roll_no, name, dob, gender, phone
            FROM students
            WHERE roll_no = %s
        """, (id,))

        student = mc.fetchone()

        if student is None:
            return jsonify({"message": "Student not found"}), 404

        if student["dob"]:
            student["dob"] = student["dob"].isoformat()

        return jsonify(student)

    finally:
        mc.close()
        mydb.close()


# API: ADD NEW STUDENT
@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True) or {}

    required = ["roll_no", "name", "dob", "gender", "phone"]

    if any(data.get(field) in (None, "") for field in required):
        return jsonify({
            "message": "Please provide all student details"
        }), 400

    mydb = config.connect()
    mc = mydb.cursor()

    try:
        mc.execute("""
            INSERT INTO students
                (roll_no, name, dob, gender, phone)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data["roll_no"],
            data["name"],
            data["dob"],
            data["gender"],
            data["phone"]
        ))

        mydb.commit()

        return jsonify({
            "message": "Student added successfully",
            "roll_no": data["roll_no"]
        }), 201

    except Exception as e:
        mydb.rollback()
        return jsonify({"message": str(e)}), 400

    finally:
        mc.close()
        mydb.close()


if __name__ == "__main__":
    app.run(debug=True)
