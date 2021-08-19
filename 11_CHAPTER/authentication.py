active_users = {
    #   FORMAT
    # 'username CAPS-LOCK':'password case-sensitive'
    'USER1':'password123',
    'USER2':'secret123',
}
def user_sanitizer(usernamell, passwordll, authll):
    """Cleans the input of the Username & password"""
    if (authll):
            if (authll == 'POLARICE'):
                print(f"\n[+] CAPTCHA CORRECT!\n")
                for item1 in active_users:
                    userll = item1
                    if(userll.upper() == user_input1.upper()):
                            namell = userll.upper()
                            auth = namell
            else:
                print(f"\nNo Auth Detected\n")
                print(f"{usernamell, passwordll}")
                exit(0)
    return auth
match1 = False
match2 = False
print(f"\t[+]==============[+]")
print(f"\t: : Login Online : :")
print(f"\t: : V1.1         : :")
print(f"\t[+]==============[+]\n\n")
print(f" + Authorization + ")
auth3 = input("$\tCODE # - > ")
print(f" + USERNAME + ")
user_input1 = input("$\t - > ")
print(f" + PASSWORD + ")
user_input2 = input("#\t - > ")
# Code -> auth3 | username - > user_input1 | password - > user_input2
block1_Og = user_sanitizer(user_input1, user_input2, auth3)
binn1 = user_input1.upper()
if(block1_Og == binn1):
    match1 = True
    if(match1 != False):
        passwrd1 = active_users[binn1]
        if(user_input2 == passwrd1):
            match2 = True
else:
    print(f"\tUsername -> FAILED")
    print(f"\tPassword -> FAILED")
    exit(1)