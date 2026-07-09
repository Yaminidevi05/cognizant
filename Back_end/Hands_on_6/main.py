from fastapi import FastAPI, Depends, HTTPException, status  # type: ignore
# sqlalchemy.ext.asyncio may not be resolved by some linters; silence with type: ignore
from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from database import engine, Base, get_db
import models
import crud
import schemas


app = FastAPI(
    title="Course Management API",
    version="1.0"
)


@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():

    return {"message": "API running"}


@app.post(
    "/api/courses/",
    response_model=schemas.CourseResponse
)
async def create_course(
        course: schemas.CourseCreate,
        db: AsyncSession = Depends(get_db)
):

    return await crud.create_course(db, course)


@app.get(
    "/api/courses/{course_id}",
    response_model=schemas.CourseResponse
)
async def get_course(
        course_id: int,
        db: AsyncSession = Depends(get_db)
):

    course = await crud.get_course(db, course_id)

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.get(
    "/api/courses/",
    response_model=list[schemas.CourseResponse]
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


@app.put(
    "/api/courses/{course_id}",
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


@app.delete("/api/courses/{course_id}")
async def delete_course(
        course_id: int,
        db: AsyncSession = Depends(get_db)
):

    success = await crud.delete_course(db, course_id)

    if not success:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return {"message": "Course deleted successfully"}