from flask import Flask, request, jsonify  # type: ignore[import]  # pylint: disable=import-error
import requests

app = Flask(__name__)

# Service URLs
COURSE_SERVICE = "http://localhost:5001"
STUDENT_SERVICE = "http://localhost:5002"


# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return "API Gateway Running"


# -----------------------------
# Course Service Proxy
# -----------------------------
@app.route("/api/courses", methods=["GET", "POST"])
@app.route("/api/courses/<path:path>", methods=["GET", "PUT", "DELETE"])
def course_proxy(path=""):

    url = f"{COURSE_SERVICE}/api/courses"
    if path:
        url += f"/{path}"

    try:
        response = requests.request(
            method=request.method,
            url=url,
            headers={key: value for key, value in request.headers if key != "Host"},
            json=request.get_json(silent=True)
        )

        return (
            response.content,
            response.status_code,
            response.headers.items()
        )

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service Unavailable"
        }), 503


# -----------------------------
# Student Service Proxy
# -----------------------------
@app.route("/api/students", methods=["GET", "POST"])
@app.route("/api/students/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def student_proxy(path=""):

    url = f"{STUDENT_SERVICE}/api/students"
    if path:
        url += f"/{path}"

    try:
        response = requests.request(
            method=request.method,
            url=url,
            headers={key: value for key, value in request.headers if key != "Host"},
            json=request.get_json(silent=True)
        )

        return (
            response.content,
            response.status_code,
            response.headers.items()
        )

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Student Service Unavailable"
        }), 503


if __name__ == "__main__":
    app.run(port=5000, debug=True)