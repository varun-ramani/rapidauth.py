import bcrypt

from database import add_user, get_user

def register(username, password):
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    add_user(username, hashed_password)

def login(username, password):
    user = get_user(username)

    if user == None:
        return