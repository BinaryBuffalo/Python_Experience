import json

# Load the username, if it has been stored perviously.
# Otherwise, prompt for the username and store it.
filename = 'userdata.json'
try:
    with open(filename) as f1:
        username = json.load(f1)
except FileNotFoundError:
    username = input("Username: ")
    with open(filename, 'w') as f2:
        json.dump(username, f2)
        print("Goodbye, " + username + "!")
else:
    print("Welcome back, " + username + "!")