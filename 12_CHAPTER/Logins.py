active_users = {
    'USER1':'password123',
    'USER2':'secret123',
}
def problem_to_log():
    print("[x] Authentication Error")
    exit(0)

def user_sanitizer(usernamell, passwordll):
    #loops through usernames in a dictionary
    for item1 in active_users:
        userll = item1 #save the username 
        auth = "one" #Default auth 
        #capitalize the USERNAME from the dictionary & userinput
        if(userll.upper() == ui1):
                namell = userll.upper()
                auth = namell
                return auth
    return auth

match1 = False
match2 = False
print("\t[+]==============[+]")
print("\t: : Login Online : :")
print("\t: : V1.2         : :")
print("\t[+]==============[+]\n\n")
print("\t + USERNAME + ")
user_input1 = input("$\t - > ")
ui1 = user_input1.upper()
print("\t + PASSWORD + ")
user_input2 = input("#\t - > ")
# Code -> auth3 | username - > user_input1 | password - > user_input2
block1_Og = user_sanitizer(user_input1, user_input2)
#
binn1 = "HoolaHoop"
if block1_Og == "one":
    problem_to_log()
else:
    binn1 = ui1

if(block1_Og == binn1):
    #checks the username
    match1 = True
    #if match1 is True
    if(match1 != False):
                #active_users['username']
        passwrd1 = active_users[binn1]
        if(user_input2 == passwrd1):
            match2 = True
else:
    problem_to_log()

if match2 == True:
    print(f"Welcome back {ui1.title()}")
else:
    problem_to_log()