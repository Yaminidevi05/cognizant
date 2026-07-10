try:
    from pydantic import BaseModel  # type: ignore
except Exception:  # pragma: no cover - fallback when pydantic is not installed
    # Minimal fallback BaseModel to allow type-checking and simple instantiation
    class BaseModel:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

        def dict(self):
            return {k: v for k, v in self.__dict__.items()}

        def json(self):
            import json

            return json.dumps(self.dict())

        class Config:  # allow nested Config classes in schema definitions
            from_attributes = False
from typing import Optional


class CourseBase(BaseModel):
    name: str
    code: str
    description: str


class CourseCreate(CourseBase):
    pass


# Used for PUT (all fields required)
class CourseUpdate(CourseBase):
    pass


# Used for PATCH (all fields optional)
class CoursePatch(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None


class CourseResponse(CourseBase):
    id: int

    class Config:
        from_attributes = True