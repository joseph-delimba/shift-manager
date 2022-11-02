from typing import Dict, List, Optional
from uuid import UUID, uuid4
from fastapi import FastAPI

from pymongo import MongoClient

from models import defaultUsers, defaultEvents, buildUser, buildShiftEvent, Gender, Role

app = FastAPI()

client = MongoClient("mongodb://rootuser:rootpass@localhost:27017")
db = client["Shift_Manager"] #database name
collectionUsers = db["users"] #collection name
collectionEvents = db["events"]

dU = defaultUsers()
dE = defaultEvents()

# Add relavent shifts to each user
for user in dU:
    for event in dE:
        if user['email'] == event['created_by'] or user['email'] == event['shift_worker']:
            user['shifts'].append(event)

for user in dU:
    collectionUsers.insert_one(user)
for event in dE:
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
    #return dU
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
    #dU.append(user)
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
    #return dE
    ret = []
    for item in collectionEvents.find({}, {"_id": 0}):
        print(item)
        ret.append(item)
    return ret

@app.post("/events")
async def register_event(
                        name: str,
                        created_by: str,
                        shift_worker: str,
                        start: str,
                        end: str,
                        timed: bool
                        ):
    if (getUser(created_by) == None) or (getUser(shift_worker) == None):
        return -1

    event = buildShiftEvent(
        name,
        created_by,
        shift_worker,
        start,
        end,
        timed)
    collectionEvents.insert_one(event)
    return 1