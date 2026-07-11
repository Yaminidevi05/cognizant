"""Database instance for the student_service.

Attempt to import flask_sqlalchemy.SQLAlchemy; if the package isn't
available (e.g. in static analysis or constrained environments), provide
a lightweight fallback so tools and tests depending on this module don't
fail at import time.
"""

import importlib

try:
    flask_sqlalchemy = importlib.import_module("flask_sqlalchemy")
    SQLAlchemy = flask_sqlalchemy.SQLAlchemy
except ImportError:  # pragma: no cover - fallback for environments without package
    class SQLAlchemy:  # minimal stub compatible with typical usage in tests/lint
        def __init__(self, *args, **kwargs):
            pass


db = SQLAlchemy()