import pyrebase.pyrebase as pyrebase

# Firebase configuration is taken from the Firebase project settings
# Firebase project settings -> General -> Your apps -> Firebase SDK snippet -> Config

config = {
    "apiKey": "AIzaSyAZb2w2kn5Gwqayx2alBWkqDZdlUbI69LU",
    "authDomain": "omegahome-4bfbb.firebaseapp.com",
    "projectId": "omegahome-4bfbb",
    "storageBucket": "omegahome-4bfbb.appspot.com",
    "messagingSenderId": "506125983254",
    "appId": "1:506125983254:web:09f9075d982ebc6e135f37",
    "measurementId": "G-1HMXHD48JQ",
    "databaseURL": "https://omegahome-4bfbb-default-rtdb.firebaseio.com"
}

# create an instance of the firebase
firebase = pyrebase.initialize_app(config)
# create an instance of the authentication service
auth = firebase.auth()


def getjwt(email, password):
    '''
    This function returns the JWT token for the user
    :param email:
    :param password:
    :return:
    '''
    user = auth.sign_in_with_email_and_password(email, password)

    return user
