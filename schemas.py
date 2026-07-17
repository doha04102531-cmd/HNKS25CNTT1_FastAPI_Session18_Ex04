from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class StudentBase(BaseModel):
    student_code: str
    full_name: str
    email: EmailStr
    status: Optional[str] = "ACTIVE"

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True


# --- SCHEMAS CHO WORKSHOP ---
class WorkshopBase(BaseModel):
    title: str
    description: Optional[str] = None
    maximum_participants: int
    status: Optional[str] = "OPEN"
    start_time: datetime

class WorkshopCreate(WorkshopBase):
    pass

class WorkshopResponse(WorkshopBase):
    id: int

    class Config:
        from_attributes = True


class RegistrationCreate(BaseModel):
    student_id: int
    workshop_id: int

class RegistrationResponse(BaseModel):
    id: int
    student_id: int
    workshop_id: int
    registered_at: datetime
    status: str

    class Config:
        from_attributes = True


class StudentWithWorkshops(StudentResponse):
    workshops: List[WorkshopResponse] = []

class WorkshopWithStudents(WorkshopResponse):
    students: List[StudentResponse] = []
