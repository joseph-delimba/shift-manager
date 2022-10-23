from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    employer = "employer"
    employee = "employee"

class ShiftEvent(BaseModel):
    created_by: str
    shift_worker: str
    day: int
    month: int
    year: int
    start_time: str
    end_time: str
    id: Optional[UUID] = uuid4()

class User(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    gender: Gender
    role: Role
    shifts: List[ShiftEvent]
