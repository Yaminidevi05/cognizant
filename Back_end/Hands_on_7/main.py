from fastapi import (  # type: ignore[import]
    FastAPI,
    Depends,
    HTTPException,
    BackgroundTasks,
    Response,
    status
)

from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from database import engine, Base, get_db
import models
import crud
import schemas
# ===========================================
# OpenAPI Customisation
# ===========================================

app = FastAPI(

    title="Course Management API",

    description="""
A FastAPI Course Management System

Features

✔ CRUD Operations

✔ Dependency Injection

✔ Background Tasks

✔ OpenAPI Documentation

✔ SQLAlchemy Async ORM

✔ HTTPException Handling

✔ Student Enrollment
""",

    version="2.0",

    contact={

        "name": "Python Backend Team",

        "email": "support@example.com"

    }

)


# ===========================================
# Startup
# ===========================================

@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )


# ===========================================
# Background Task
# ===========================================

def send_confirmation_email(email: str):

    print(
        f"Sending confirmation to {email}"
    )


# ===========================================
# Root
# ===========================================

@app.get("/")
async def home():

    return {

        "message": "Course Management API Running"

    }


# ===========================================
# COURSE CRUD
# ===========================================

@app.post(
    "/api/courses/",
    tags=["Courses"],
    summary="Create Course",
    response_description="Created Course",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.CourseResponse
)
async def create_course(

        course: schemas.CourseCreate,

        db: AsyncSession = Depends(get_db)

):

    return await crud.create_course(
        db,
        course
    )


@app.get(
    "/api/courses/",
    tags=["Courses"],
    response_model=list[
        schemas.CourseResponse
    ]
)
async def get_courses(

        skip: int = 0,

        limit: int = 10,

        department_id: int | None = None,

        db: AsyncSession = Depends(get_db)

):

    return await crud.get_courses(

        db,

        skip,

        limit,

        department_id

    )


@app.get(
    "/api/courses/{course_id}",
    tags=["Courses"],
    response_model=schemas.CourseResponse
)
async def get_course(

        course_id: int,

        db: AsyncSession = Depends(get_db)

):

    course = await crud.get_course(
        db,
        course_id
    )

    if course is None:

        raise HTTPException(

            status_code=404,

            detail="Course not found"

        )

    return course


@app.put(
    "/api/courses/{course_id}",
    tags=["Courses"],
    response_model=schemas.CourseResponse
)
async def update_course(

        course_id: int,

        course: schemas.CourseUpdate,

        db: AsyncSession = Depends(get_db)

):

    updated = await crud.update_course(

        db,

        course_id,

        course

    )

    if updated is None:

        raise HTTPException(

            status_code=404,

            detail="Course not found"

        )

    return updated


@app.delete(
    "/api/courses/{course_id}",
    tags=["Courses"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(

        course_id: int,

        db: AsyncSession = Depends(get_db)

):

    success = await crud.delete_course(
        db,
        course_id
    )

    if not success:

        raise HTTPException(

            status_code=404,

            detail="Course not found"

        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )


# ===========================================
# Students in Course (JOIN)
# ===========================================

@app.get(
    "/api/courses/{course_id}/students/",
    tags=["Courses"],
    response_model=list[
        schemas.StudentResponse
    ]
)
async def get_students_in_course(

        course_id: int,

        db: AsyncSession = Depends(get_db)

):

    return await crud.get_students_by_course(

        db,

        course_id

    )


# ===========================================
# STUDENT CRUD
# ===========================================

@app.post(
    "/api/students/",
    tags=["Students"],
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.StudentResponse
)
async def create_student(

        student: schemas.StudentCreate,

        db: AsyncSession = Depends(get_db)

):

    return await crud.create_student(

        db,

        student

    )


@app.get(
    "/api/students/",
    tags=["Students"],
    response_model=list[
        schemas.StudentResponse
    ]
)
async def get_students(

        db: AsyncSession = Depends(get_db)

):

    return await crud.get_students(db)


@app.get(
    "/api/students/{student_id}",
    tags=["Students"],
    response_model=schemas.StudentResponse
)
async def get_student(

        student_id: int,

        db: AsyncSession = Depends(get_db)

):

    student = await crud.get_student(

        db,

        student_id

    )

    if student is None:

        raise HTTPException(

            status_code=404,

            detail="Student not found"

        )

    return student
@app.put(
    "/api/students/{student_id}",
    tags=["Students"],
    response_model=schemas.StudentResponse
)
async def update_student(
        student_id: int,
        student: schemas.StudentUpdate,
        db: AsyncSession = Depends(get_db)
):

    updated = await crud.update_student(
        db,
        student_id,
        student
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated


@app.delete(
    "/api/students/{student_id}",
    tags=["Students"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_student(
        student_id: int,
        db: AsyncSession = Depends(get_db)
):

    success = await crud.delete_student(
        db,
        student_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )


# ===========================================
# ENROLLMENT CRUD
# ===========================================

@app.post(
    "/api/enrollments/",
    tags=["Enrollments"],
    summary="Create Enrollment",
    response_description="Enrollment Created",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.EnrollmentResponse
)
async def create_enrollment(
        enrollment: schemas.EnrollmentCreate,
        background_tasks: BackgroundTasks,
        db: AsyncSession = Depends(get_db)
):

    student = await crud.get_student(
        db,
        enrollment.student_id
    )

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    course = await crud.get_course(
        db,
        enrollment.course_id
    )

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    new_enrollment = await crud.create_enrollment(
        db,
        enrollment
    )

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment


@app.get(
    "/api/enrollments/",
    tags=["Enrollments"],
    response_model=list[
        schemas.EnrollmentResponse
    ]
)
async def get_enrollments(
        db: AsyncSession = Depends(get_db)
):

    return await crud.get_enrollments(db)


@app.get(
    "/api/enrollments/{enrollment_id}",
    tags=["Enrollments"],
    response_model=schemas.EnrollmentResponse
)
async def get_enrollment(
        enrollment_id: int,
        db: AsyncSession = Depends(get_db)
):

    enrollment = await crud.get_enrollment(
        db,
        enrollment_id
    )

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


@app.delete(
    "/api/enrollments/{enrollment_id}",
    tags=["Enrollments"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_enrollment(
        enrollment_id: int,
        db: AsyncSession = Depends(get_db)
):

    success = await crud.delete_enrollment(
        db,
        enrollment_id
    )

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT
    )