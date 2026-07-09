try:
	from flask_sqlalchemy import SQLAlchemy  # type: ignore
	db = SQLAlchemy()
except (ImportError, ModuleNotFoundError):  # pragma: no cover
	SQLAlchemy = None
	db = None

try:
	from flask_migrate import Migrate  # type: ignore
	migrate = Migrate()
except (ImportError, ModuleNotFoundError):  # pragma: no cover
	Migrate = None
	migrate = None