from typing import Dict, List, Optional
from uuid import UUID, uuid4
from fastapi import FastAPI

from pymongo import MongoClient

from models import Gender, Role, User, ShiftEvent

app = FastAPI()

client = MongoClient("mongodb://rootuser:rootpass@localhost:27017")
db = client["Shift_Manager"] #database name
collectionUsers = db["users"] #collection name
collectionEvents = db["events"]

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
        created_by,
        shift_worker,
        day,
        month,
        year,
        start_time,
        end_time):
    return {
        "created_by": created_by,
        "shift_worker": shift_worker,
        "day": day,
        "month": month,
        "year": year,
        "start_time": start_time,
        "end_time": end_time
    }

defaultUsers: List[dict] = [
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

defaultEvents: List[dict] = [
    buildShiftEvent(
        created_by="Peyton@gmail.com",
        shift_worker="Kolla@gmail.com",
        day=12,
        month=1,
        year=2023,
        start_time="9:00",
        end_time="5:00"
    ),
    buildShiftEvent(
        created_by="Peyton@gmail.com",
        shift_worker="Kolla@gmail.com",
        day=13,
        month=1,
        year=2023,
        start_time="9:00",
        end_time="5:00"
    ),
    buildShiftEvent(
        created_by="Peyton@gmail.com",
        shift_worker="Kolla@gmail.com",
        day=14,
        month=1,
        year=2023,
        start_time="9:00",
        end_time="5:00"
    ),
    buildShiftEvent(
        created_by="Peyton@gmail.com",
        shift_worker="Teh@gmail.com",
        day=15,
        month=1,
        year=2023,
        start_time="9:00",
        end_time="5:00"
    ),
    buildShiftEvent(
        created_by="Peyton@gmail.com",
        shift_worker="Teh@gmail.com",
        day=16,
        month=1,
        year=2023,
        start_time="9:00",
        end_time="5:00"
    ),
    buildShiftEvent(
        created_by="Peyton@gmail.com",
        shift_worker="Teh@gmail.com",
        day=17,
        month=1,
        year=2023,
        start_time="9:00",
        end_time="5:00"
    )
]

# Add relavent shifts to each user
for user in defaultUsers:
    for event in defaultEvents:
        if user['email'] == event['created_by'] or user['email'] == event['shift_worker']:
            user['shifts'].append(event)

for user in defaultUsers:
    collectionUsers.insert_one(user)
for event in defaultEvents:
    collectionEvents.insert_one(event)

def getUser(userEmail: str):
    for user in collectionUsers.find():
        if user['email'] == userEmail:
            return user
    return None

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/users")
async def fetch_users():
    #return defaultUsers
    ret = []
    for item in collectionUsers.find({}, {"_id": 0}):
        ret.append(item)
    return ret

@app.post("/users")
async def register_user(
                        email: str,
                        password: str,
                        first_name: str,
                        last_name: str,
                        gender: Gender,
                        role: Role
                        ):
    dupCheck = getUser(email)
    if dupCheck != None:
        return 0
    user = buildUser(
            email,
            password,
            first_name,
            last_name,
            gender,
            role)
    #defaultUsers.append(user)
    collectionUsers.insert_one(user)
    return 1


@app.get("/login")
async def login(email: str, password: str):
    user = getUser(email)
    if(user == None):
        return 0
    if(user['password'] != password):
        return 0
    return user


@app.get("/events")
async def fetch_events():
    #return defaultEvents
    ret = []
    for item in collectionEvents.find({}, {"_id": 0}):
        print(item)
        ret.append(item)
    return ret

@app.post("/events")
async def register_event(
                        created_by: str,
                        shift_worker: str,
                        day: int,
                        month: int,
                        year: int,
                        start_time: str,
                        end_time: str
                        ):
    if (getUser(created_by) == None) or (getUser(shift_worker) == None):
        return -1

    if (day > 31 or day < 1) or (month > 12 or month < 1):
        return -1

    event = buildShiftEvent(
        created_by,
        shift_worker,
        day,
        month,
        year,
        start_time,
        end_time)
    collectionEvents.insert_one(event)
    return 1