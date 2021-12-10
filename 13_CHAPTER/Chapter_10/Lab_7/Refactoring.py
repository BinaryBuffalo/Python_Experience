import json, sys

def greet_user():
    """Greats the User"""
    filename = 'userdata.json'
    try:
        with open(filename) as f1:
            username = json.load(f1)
    except FileNotFoundError:
        username = input("Username: ")
        with open(filename, 'w') as f2:
            json.dump(username, f2)
            print("We will remember You Next time " + username + "!")
            sys.exit()
    else:
        print("Welcome back, " + username + ".")

def get_stored_username():
    """Get stored username if availiable"""
    filename = 'userdata.json'
    try:
        with open(filename) as f1:
            username = json.load(f1)
        pass
    except FileNotFoundError:
        return None
    else:
        return username

greet_user()
obj_1 = get_stored_username()
if obj_1 == None:
    print("Failed to find username")
    sys.exit()
else:
    print("username -> " + obj_1)
    pass