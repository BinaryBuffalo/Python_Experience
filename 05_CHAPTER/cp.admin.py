#Author: Baked Binary
#Usage: Public/Authentication | LV 1
# Checks a list for usernames & admin with
# an empty list failsafe & 0.1sec forloop
import time
active_users = ["dave", "dan", "george", "admin", "tom"]
username = "dave"
for user in active_users:
    if username == 'admin':
        safe_username = "ADMIN"
    if username in user:
        safe_username = username
    elif username not in user:
        safe_username = "NULL"
    else:
        print(f"Failed to authenticate List is empty")
        exit(0)
if safe_username == "ADMIN":
    print(f"hello {safe_username} you are admin")
elif safe_username  == username:
    print(f"Welcome back, {safe_username}")
else:
     print("authentication failure")