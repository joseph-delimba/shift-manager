#must pip install pyrebase4
import requests
import pyrebase
import json

firebaseConfig={  
    'apiKey': "AIzaSyAyrcPx1O7lS2lvBMWIFL-9TY06ZMiACjI",
    'authDomain': "shift-manager-e30cf.firebaseapp.com",
    'projectId': "shift-manager-e30cf",
    'storageBucket': "shift-manager-e30cf.appspot.com",
    'messagingSenderId': "283448715505",
    'appId': "1:283448715505:web:4ba35d0605486df3ace150",
    'measurementId': "G-9Y52X0KKX7",
    'databaseURL': ""}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#attempts to create a user w/ the given email and password,
#returns unique user id string if successful,
#"EMAIL_EXISTS", "WEAK_PASSWORD : Password should be at least 6 characters", or "INVALID_EMAIL" if not
def signup(email: str, password: str):
    try:
        user = auth.create_user_with_email_and_password(email,password)
        #CODE FOR SUCCESSFUL SIGNUP
        #add user to database, move them to the schedule page?
        print("User successfully created!")
        return user['localId']
    except requests.exceptions.HTTPError as e:
        #CODE FOR FAILED SIGNUP
        #display error message, allow them to try again
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        return error

#attempts to login a user w/ the given email and password,
#returns unique user id string if successful,
#"INVALID_PASSWORD" or "EMAIL_NOT_FOUND" if not
def login(email: str, password: str):
    try:
        login = auth.sign_in_with_email_and_password(email,password)
        #CODE FOR SUCCESSFUL LOGIN
        #move them to the schedule page, display users shifts from the database?
        print("Successfully logged in!")
        return login['localId']
    except requests.exceptions.HTTPError as e:
        #CODE FOR FAILED LOGIN
        #display error message
        error_json = e.args[1]
        error = json.loads(error_json)['error']['message']
        return error
