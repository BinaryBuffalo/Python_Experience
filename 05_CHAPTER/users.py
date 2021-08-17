#   Author: BakedBinary
my_list1 = ["Dan","Man","Tan","Foo"]
my_list2 = ["Bar","Baz","zoo","Foo"]
i = 0
for users in my_list1:
    users.lower()
    if users in my_list2:
        print(f"Username: {users} ->Taken")
        opt1 = True
        taken_username = users
    elif users not in my_list2:
        print(f"username: {users} ->Valid ")
        opt2 = True
        valid_username = users
    else:
        print("List Empty")

if opt1:
    print(f"Taken Usernames {taken_username}")
if opt2:
    print(f"Valid usernames {valid_username}")

