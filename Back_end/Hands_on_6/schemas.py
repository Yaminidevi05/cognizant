try:
    from pydantic import BaseModel  # type: ignore
except Exception:  # fallback for editors/linters when pydantic isn't installed
    # Minimal fallback so static analysis or editors don't mark the import as unresolved.
    class BaseModel:  # type: ignore
        pass
from typing import Optional, List


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


class DepartmentResponse(BaseModel):
    id: int
    name: str
    courses: List[CourseResponse] = []

    class Config:
        from_attributes = True