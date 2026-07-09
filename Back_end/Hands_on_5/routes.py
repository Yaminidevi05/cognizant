from flask import Blueprint, request, jsonify  # type: ignore[import]
from extensions import db
from courses.models import Course, Student, Enrollment

course_bp = Blueprint("course_bp", __name__)


@course_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])


@course_bp.route("/<int:id>/", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict())


@course_bp.route("/", methods=["POST"])
def add_course():
    data = request.get_json()

    course = Course(
        title=data["title"],
        description=data["description"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


@course_bp.route("/<int:id>/", methods=["PUT"])
def update_course(id):
    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.title = data.get("title", course.title)
    course.description = data.get("description", course.description)
    course.department_id = data.get("department_id", course.department_id)

    db.session.commit()

    return jsonify(course.to_dict())


@course_bp.route("/<int:id>/", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "message": "Course deleted successfully"
    })


@course_bp.route("/<int:id>/students/", methods=["GET"])
def get_students(id):

    Course.query.get_or_404(id)

    students = (
        db.session.query(Student)
        .join(Enrollment)
        .filter(Enrollment.course_id == id)
        .all()
    )

    return jsonify(
        [student.to_dict() for student in students]
    )