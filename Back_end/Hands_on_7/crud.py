try:
    # Preferred import (SQLAlchemy 1.4+)
    from sqlalchemy import select  # type: ignore
except ImportError:
    # Fallback for environments where sqlalchemy export resolution differs
    from sqlalchemy.sql import select  # type: ignore

from models import Course, Student, Enrollment


# =====================================================
# COURSE CRUD
# =====================================================

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
        select(Course).where(
            Course.id == course_id
        )
    )

    return result.scalar_one_or_none()


async def get_courses(
        db,
        skip=0,
        limit=10,
        department_id=None
):

    query = select(Course)

    if department_id is not None:
        query = query.where(
            Course.department_id == department_id
        )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


async def update_course(
        db,
        course_id,
        course
):

    existing = await get_course(
        db,
        course_id
    )

    if existing is None:
        return None

    for key, value in course.dict(
            exclude_unset=True
    ).items():
        setattr(existing, key, value)

    await db.commit()

    await db.refresh(existing)

    return existing


async def delete_course(
        db,
        course_id
):

    existing = await get_course(
        db,
        course_id
    )

    if existing is None:
        return False

    await db.delete(existing)

    await db.commit()

    return True


async def get_students_by_course(
        db,
        course_id
):

    result = await db.execute(

        select(Student)

        .join(Enrollment)

        .where(
            Enrollment.course_id == course_id
        )

    )

    return result.scalars().all()


# =====================================================
# STUDENT CRUD
# =====================================================

async def create_student(
        db,
        student
):

    obj = Student(
        name=student.name,
        email=student.email,
        age=student.age
    )

    db.add(obj)

    await db.commit()

    await db.refresh(obj)

    return obj


async def get_student(
        db,
        student_id
):

    result = await db.execute(

        select(Student).where(
            Student.id == student_id
        )

    )

    return result.scalar_one_or_none()


async def get_students(db):

    result = await db.execute(
        select(Student)
    )

    return result.scalars().all()


async def update_student(
        db,
        student_id,
        student
):

    obj = await get_student(
        db,
        student_id
    )

    if obj is None:
        return None

    for key, value in student.dict(
            exclude_unset=True
    ).items():
        setattr(obj, key, value)

    await db.commit()

    await db.refresh(obj)

    return obj


async def delete_student(
        db,
        student_id
):

    obj = await get_student(
        db,
        student_id
    )

    if obj is None:
        return False

    await db.delete(obj)

    await db.commit()

    return True


# =====================================================
# ENROLLMENT CRUD
# =====================================================

async def create_enrollment(
        db,
        enrollment
):

    obj = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id
    )

    db.add(obj)

    await db.commit()

    await db.refresh(obj)

    return obj


async def get_enrollment(
        db,
        enrollment_id
):

    result = await db.execute(

        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )

    )

    return result.scalar_one_or_none()


async def get_enrollments(db):

    result = await db.execute(
        select(Enrollment)
    )

    return result.scalars().all()


async def delete_enrollment(
        db,
        enrollment_id
):

    obj = await get_enrollment(
        db,
        enrollment_id
    )

    if obj is None:
        return False

    await db.delete(obj)

    await db.commit()

    return True