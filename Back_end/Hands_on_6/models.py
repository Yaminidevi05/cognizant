from sqlalchemy import Column, Integer, String, ForeignKey  # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    courses = relationship("Course", back_populates="department")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    credits = Column(Integer)

    department_id = Column(Integer, ForeignKey("departments.id"))

    department = relationship("Department", back_populates="courses")