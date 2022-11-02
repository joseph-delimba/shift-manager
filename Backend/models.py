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

def buildUser(
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        gender: Gender,
        role: Role):
    return {
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "role": role,
        "shifts": []
    }

def buildShiftEvent(
        name,
        created_by,
        shift_worker,
        start,
        end,
        timed
        ):
    return {
        "name": name,
        "created_by": created_by,
        "shift_worker": shift_worker,
        "start": start,
        "end": end,
        "timed": timed
    }

def defaultUsers():
    ret = [
        buildUser(
            email="Peyton@gmail.com",
            password="password",
            first_name="Peyton",
            last_name="Nill",
            gender=Gender.female,
            role=Role.employee
        ),
        buildUser(
            email="Kolla@gmail.com",
            password="password",
            first_name="Kolla",
            last_name="Nill",
            gender=Gender.female,
            role=Role.employee
        ),
        buildUser(
            email="Teh@gmail.com",
            password="password",
            first_name="Teh",
            last_name="Nill",
            gender=Gender.male,
            role=Role.employee
        ),
    ]
    return ret

def defaultEvents():
    ret = [
        buildShiftEvent(
            name="Shift Event 1",
            created_by="Peyton@gmail.com",
            shift_worker="Kolla@gmail.com",
            start="Thu Jan 12 2023 9:00:00 GMT-0400 (Eastern Daylight Time)",
            end="Thu Jan 12 2023 17:00:00 GMT-0400 (Eastern Daylight Time)",
            timed=True
        ),
        buildShiftEvent(
            name="Shift Event 2",
            created_by="Peyton@gmail.com",
            shift_worker="Kolla@gmail.com",
            start="Fri Jan 13 2023 9:00:00 GMT-0400 (Eastern Daylight Time)",
            end="Fri Jan 13 2023 17:00:00 GMT-0400 (Eastern Daylight Time)",
            timed=True
        ),
        buildShiftEvent(
            name="Shift Event 3",
            created_by="Peyton@gmail.com",
            shift_worker="Kolla@gmail.com",
            start="Sat Jan 14 2023 9:00:00 GMT-0400 (Eastern Daylight Time)",
            end="Sat Jan 14 2023 17:00:00 GMT-0400 (Eastern Daylight Time)",
            timed=True
        ),
        buildShiftEvent(
            name="Shift Event 4",
            created_by="Peyton@gmail.com",
            shift_worker="Teh@gmail.com",
            start="Sun Jan 15 2023 9:00:00 GMT-0400 (Eastern Daylight Time)",
            end="Sun Jan 15 2023 17:00:00 GMT-0400 (Eastern Daylight Time)",
            timed=True
        ),
        buildShiftEvent(
            name="Shift Event 5",
            created_by="Peyton@gmail.com",
            shift_worker="Teh@gmail.com",
            start="Mon Jan 16 2023 9:00:00 GMT-0400 (Eastern Daylight Time)",
            end="Mon Jan 16 2023 17:00:00 GMT-0400 (Eastern Daylight Time)",
            timed=True
        ),
        buildShiftEvent(
            name="Shift Event 6",
            created_by="Peyton@gmail.com",
            shift_worker="Teh@gmail.com",
            start="Tue Jan 17 2023 9:00:00 GMT-0400 (Eastern Daylight Time)",
            end="Tue Jan 17 2023 17:00:00 GMT-0400 (Eastern Daylight Time)",
            timed=True
        )
    ]
    return ret
