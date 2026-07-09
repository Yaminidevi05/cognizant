try:
    from sqlalchemy import Column, Integer, String, ForeignKey  # type: ignore[import]
    from sqlalchemy.orm import relationship  # type: ignore[import]
except ImportError as exc:
    raise ImportError(
        "SQLAlchemy is required to run this module. Install it with 'pip install sqlalchemy'."
    ) from exc

from database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    courses = relationship(
        "Course",
        back_populates="department",
        cascade="all, delete"
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course",
        cascade="all, delete"
    )


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer)

    enrollments = relationship(
        "Enrollment",
        back_populates="student",
        cascade="all, delete"
    )


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id")
    )

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )