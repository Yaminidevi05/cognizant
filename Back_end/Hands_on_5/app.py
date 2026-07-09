from flask import Flask  # type: ignore[import]
from config import Config
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from courses.routes import course_bp
    app.register_blueprint(course_bp, url_prefix="/api/courses")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)