#Author: Baked Binary
#Usage: Public/Authentication | LV 1
# Checks a list for usernames & admin with
# an empty list failsafe & 0.1sec forloop
import time
active_users = ["dave", "dan", "george", "admin", "tom"]
username = "admin"
for user in active_users:
    if username == 'admin':
        print(f"Hello, Welcome {username} would you like to see a status report?")
        exit(0)
    if username in user:
        print(f"Welcome, back {user}")
        exit(0)
    elif username not in user:
        print('\033c')
    else:
        print(f"Failed to authenticate List is empty")
        exit(0)
print(f"Failed to authenticate")