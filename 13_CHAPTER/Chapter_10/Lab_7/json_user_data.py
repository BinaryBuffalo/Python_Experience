import json

username = input("USERNAME: ")
filename = 'userdata.json'
print("[!] Writing to userdata.json")
with open(filename, 'w') as f1:
    json.dump(username, f1)
print("[!] Reading userdata.json")
with open(filename) as f2:
    username = json.load(f2)
print("Welcome back, " + username + "!")