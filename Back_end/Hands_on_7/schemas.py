try:
    from pydantic import BaseModel  # type: ignore[import]
except ImportError:
    class BaseModel:
        pass

from typing import Optional, List


# ------------------------
# COURSE
# ------------------------

class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(BaseModel):
    id: int
    name: str
    code: str
    credits: int
    department_id: int

    class Config:
        from_attributes = True


# ------------------------
# DEPARTMENT
# ------------------------

class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: List[CourseResponse] = []

    class Config:
        from_attributes = True


# ------------------------
# STUDENT
# ------------------------

class StudentCreate(BaseModel):
    name: str
    email: str
    age: int


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int

    class Config:
        from_attributes = True


# ------------------------
# ENROLLMENT
# ------------------------

class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int

    class Config:
        from_attributes = True