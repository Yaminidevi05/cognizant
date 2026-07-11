from pydantic import BaseModel, EmailStr  # type: ignore[import]

class CourseBase(BaseModel):
    name: str
    instructor: str
    duration: int


class CourseCreate(CourseBase):
    pass


class CourseOut(CourseBase):
    id: int

    class Config:
        from_attributes = True


# -------------------- USER --------------------

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True


# -------------------- TOKEN --------------------

class Token(BaseModel):
    access_token: str
    token_type: str