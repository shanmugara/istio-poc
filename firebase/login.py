import pyrebase
from config import config

user = "shan.raj@gmail.com"
password = "N0!is2Kn0w"

def login(user=user, password=password):
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    try:
        user = auth.sign_in_with_email_and_password(user, password)
        return user
    except:
        print("Invalid email or password")
