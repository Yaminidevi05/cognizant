from fastapi import FastAPI, Depends, HTTPException, Response, status, Request  # type: ignore[import]
from fastapi.responses import JSONResponse  # type: ignore[import]
# Import Session from SQLAlchemy ORM session path.
from sqlalchemy.orm.session import Session  # type: ignore[import]

import crud
import models
import schemas
from database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Management API",
    version="1.0.0",
    description="Hands-On 8 - RESTful API Design Best Practices"
)

# -------------------------------------------------------
# API Versioning Strategies:
#
# 1. URL Versioning:
#    /api/v1/courses
#
# 2. Header Versioning:
#    Accept: application/vnd.api+json;version=1
#
# URL versioning is easier to understand and test.
# Header versioning keeps URLs clean but requires
# clients to send custom headers.
# -------------------------------------------------------


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Standard Error Response
def error_response(code: str, message: str, field=None):
    return {
        "error": {
            "code": code,
            "message": message,
            "field": field
        }
    }


# -----------------------------
# 404 Error Handler
# -----------------------------
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return JSONResponse(
        status_code=404,
        content=error_response(
            "NOT_FOUND",
            "Requested resource does not exist"
        )
    )


# -----------------------------
# Home
# -----------------------------
@app.get("/")
def home():
    return {"message": "Course Management API is Running"}


# -----------------------------
# GET ALL COURSES
# Pagination + Search
# -----------------------------
@app.get("/api/v1/courses")
def get_courses(
    page: int = 1,
    page_size: int = 10,
    search: str = None,
    db: Session = Depends(get_db)
):

    total, courses = crud.get_courses(
        db,
        page=page,
        page_size=page_size,
        search=search
    )

    next_page = None
    previous_page = None

    if page * page_size < total:
        next_page = f"/api/v1/courses?page={page+1}&page_size={page_size}"

    if page > 1:
        previous_page = f"/api/v1/courses?page={page-1}&page_size={page_size}"

    return {
        "count": total,
        "next": next_page,
        "previous": previous_page,
        "results": courses
    }


# -----------------------------
# GET COURSE BY ID
# -----------------------------
@app.get(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_200_OK
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = crud.get_course(db, course_id)

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    return course


# -----------------------------
# CREATE COURSE
# -----------------------------
@app.post(
    "/api/v1/courses",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course: schemas.CourseCreate,
    response: Response,
    db: Session = Depends(get_db)
):

    new_course = crud.create_course(db, course)

    response.headers["Location"] = f"/api/v1/courses/{new_course.id}"

    return new_course
# -----------------------------
# PUT (Full Update)
# -----------------------------
@app.put(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_200_OK
)
def update_course(
    course_id: int,
    updated_course: schemas.CourseUpdate,
    db: Session = Depends(get_db)
):

    course = crud.update_course(
        db,
        course_id,
        updated_course
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    return course


# -----------------------------
# PATCH (Partial Update)
# -----------------------------
@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_200_OK
)
def patch_course(
    course_id: int,
    course_data: schemas.CoursePatch,
    db: Session = Depends(get_db)
):

    course = crud.patch_course(
        db,
        course_id,
        course_data
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    return course


# -----------------------------
# DELETE COURSE
# -----------------------------
@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    deleted = crud.delete_course(
        db,
        course_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail=error_response(
                "NOT_FOUND",
                f"Course with id {course_id} does not exist"
            )
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# -----------------------------
# Validation Error Handler
# -----------------------------
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):

    if isinstance(exc.detail, dict):
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.detail
        )

    return JSONResponse(
        status_code=exc.status_code,
        content=error_response(
            "HTTP_ERROR",
            str(exc.detail)
        )
    )