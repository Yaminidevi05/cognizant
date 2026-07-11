from flask import Flask, request, jsonify  # type: ignore
from database import db
from models import Course

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///course.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return "Course Service Running"


# ---------------------------
# Create Course
# ---------------------------
@app.route("/api/courses", methods=["POST"])
def create_course():

    data = request.get_json()

    course = Course(
        name=data["name"],
        department=data["department"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


# ---------------------------
# Get All Courses
# ---------------------------
@app.route("/api/courses", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    return jsonify([course.to_dict() for course in courses])


# ---------------------------
# Get Course by ID
# ---------------------------
@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    return jsonify(course.to_dict())


# ---------------------------
# Update Course
# ---------------------------
@app.route("/api/courses/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    data = request.get_json()

    course.name = data["name"]
    course.department = data["department"]

    db.session.commit()

    return jsonify(course.to_dict())


# ---------------------------
# Delete Course
# ---------------------------
@app.route("/api/courses/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get(id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted successfully"})


if __name__ == "__main__":
    app.run(port=5001, debug=True)