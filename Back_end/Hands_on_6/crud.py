from sqlalchemy import select  # type: ignore
from models import Course


async def create_course(db, course):

    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    return new_course


async def get_course(db, course_id):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    return result.scalar_one_or_none()


async def get_courses(db, skip=0, limit=10, department_id=None):

    query = select(Course)

    if department_id is not None:
        query = query.where(
            Course.department_id == department_id
        )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


async def update_course(db, course_id, course):

    existing = await get_course(db, course_id)

    if not existing:
        return None

    for key, value in course.dict(exclude_unset=True).items():
        setattr(existing, key, value)

    await db.commit()

    await db.refresh(existing)

    return existing


async def delete_course(db, course_id):

    existing = await get_course(db, course_id)

    if not existing:
        return False

    db.delete(existing)

    await db.commit()

    return True