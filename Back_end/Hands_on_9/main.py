from fastapi import FastAPI, Depends, HTTPException, status  # type: ignore
# Use Starlette's CORSMiddleware directly to avoid unresolved import warnings
from starlette.middleware.cors import CORSMiddleware  # type: ignore
from sqlalchemy.orm import Session  # type: ignore

import models
import schemas
import crud
import security

from database import engine
from auth import get_db, create_access_token, get_current_user

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Management API",
    version="1.0"
)

# -------------------- CORS --------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- AUTH --------------------

@app.post(
    "/api/v1/auth/register/",
    response_model=schemas.UserOut,
    status_code=201
)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = crud.get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    return crud.create_user(db, user)


from fastapi.security import OAuth2PasswordRequestForm  # type: ignore

@app.post("/api/v1/auth/login/", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = crud.get_user_by_email(db, form_data.username)

    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not security.verify_password(
        form_data.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# -------------------- COURSES --------------------

@app.get(
    "/api/v1/courses/",
    response_model=list[schemas.CourseOut]
)
def get_all_courses(
    db: Session = Depends(get_db)
):
    return crud.get_courses(db)


@app.post(
    "/api/v1/courses/",
    response_model=schemas.CourseOut,
    status_code=201
)
def create_course(
    course: schemas.CourseCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return crud.create_course(db, course)


@app.delete("/api/v1/courses/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    course = crud.delete_course(db, course_id)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {
        "message": "Course deleted successfully"
    }


@app.get("/")
def home():
    return {
        "message": "Hands-On 9 Authentication API is running"
    }