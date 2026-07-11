from sqlalchemy.orm import Session  # type: ignore[reportMissingImports]
from typing import Optional

import models
import schemas
import security


# ---------------- USER ----------------

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(
        models.User.email == email
    ).first()


def create_user(db: Session, user: schemas.UserCreate):

    hashed_password = security.get_password_hash(
        user.password
    )

    db_user = models.User(
        email=user.email,
        hashed_password=hashed_password,
        is_active=True
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# ---------------- COURSE ----------------

def get_courses(db: Session):
    return db.query(models.Course).all()


def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(
        models.Course.id == course_id
    ).first()


def create_course(db: Session, course: schemas.CourseCreate):

    db_course = models.Course(
        name=course.name,
        instructor=course.instructor,
        duration=course.duration
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    return db_course


def delete_course(db: Session, course_id: int):

    course = get_course(db, course_id)

    if course:
        db.delete(course)
        db.commit()

    return course