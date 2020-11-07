import json
import atexit

with open('database.json', 'r') as file:
    data = json.loads(file.read())

def add_user(username, password):
    new_user = {
        "password": password
    }

    data[username] = new_user

def get_user(username):
    try:
        return data[username]
    except:
        return None

def save_data():
    with open('database.json', 'w') as file:
        file.write(json.dumps(data, indent=4))

atexit.register(save_data)