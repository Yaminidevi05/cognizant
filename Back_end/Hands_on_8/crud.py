from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sqlalchemy.orm import Session  # type: ignore[import]
else:
    try:
        from sqlalchemy.orm import Session  # type: ignore[import]
    except Exception:
        Session = Any

try:
    import importlib
    sqlalchemy = importlib.import_module("sqlalchemy")
    or_ = sqlalchemy.or_
except Exception:  # pragma: no cover - for environments without sqlalchemy
    def or_(*args, **kwargs):
        raise RuntimeError("sqlalchemy is not installed")
import models
import schemas


# -----------------------------
# CREATE
# -----------------------------
def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(
        name=course.name,
        code=course.code,
        description=course.description
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


# -----------------------------
# GET BY ID
# -----------------------------
def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()


# -----------------------------
# GET ALL WITH PAGINATION
# -----------------------------
def get_courses(
    db: Session,
    page: int = 1,
    page_size: int = 10,
    search: str = None
):
    query = db.query(models.Course)

    # Search by course name or code
    if search:
        query = query.filter(
            or_(
                models.Course.name.ilike(f"%{search}%"),
                models.Course.code.ilike(f"%{search}%")
            )
        )

    total = query.count()

    courses = (
        query.offset((page - 1) * page_size)
        .limit(page_size)
        .all()
    )

    return total, courses


# -----------------------------
# PUT (Full Update)
# -----------------------------
def update_course(
    db: Session,
    course_id: int,
    updated_course: schemas.CourseUpdate
):
    course = get_course(db, course_id)

    if not course:
        return None

    course.name = updated_course.name
    course.code = updated_course.code
    course.description = updated_course.description

    db.commit()
    db.refresh(course)

    return course


# -----------------------------
# PATCH (Partial Update)
# -----------------------------
def patch_course(
    db: Session,
    course_id: int,
    course_data: schemas.CoursePatch
):
    course = get_course(db, course_id)

    if not course:
        return None

    update_data = course_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course


# -----------------------------
# DELETE
# -----------------------------
def delete_course(db: Session, course_id: int):
    course = get_course(db, course_id)

    if not course:
        return False

    db.delete(course)
    db.commit()

    return True