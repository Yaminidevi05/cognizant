from flask import Flask, request, jsonify  # type: ignore
from database import db
from models import Student
import requests

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Student Service Running"


# -------------------------
# Create Student
# -------------------------
@app.route("/api/students", methods=["POST"])
def create_student():

    data = request.get_json()

    student = Student(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(student)
    db.session.commit()

    return jsonify(student.to_dict()), 201


# -------------------------
# Get All Students
# -------------------------
@app.route("/api/students", methods=["GET"])
def get_students():

    students = Student.query.all()

    return jsonify([student.to_dict() for student in students])


# -------------------------
# Get Student by ID
# -------------------------
@app.route("/api/students/<int:id>", methods=["GET"])
def get_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    return jsonify(student.to_dict())


# -------------------------
# Update Student
# -------------------------
@app.route("/api/students/<int:id>", methods=["PUT"])
def update_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    data = request.get_json()

    student.name = data["name"]
    student.email = data["email"]

    db.session.commit()

    return jsonify(student.to_dict())


# -------------------------
# Delete Student
# -------------------------
@app.route("/api/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully"})


# -------------------------
# Enroll Student
# -------------------------
@app.route("/api/students/<int:id>/enroll", methods=["POST"])
def enroll_student(id):

    student = Student.query.get(id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    data = request.get_json()

    course_id = data["course_id"]

    try:

        response = requests.get(
            f"http://localhost:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({
                "message": "Course not found"
            }), 404

        course = response.json()

        return jsonify({
            "message": "Enrollment Successful",
            "student": student.to_dict(),
            "course": course
        })

    except requests.exceptions.ConnectionError:

        return jsonify({
            "message": "Course Service Unavailable"
        }), 503


if __name__ == "__main__":
    app.run(port=5002, debug=True)