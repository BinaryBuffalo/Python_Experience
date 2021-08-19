import time
active_users = {
    #   FORMAT
    # 'username CAPS-LOCK':'password case-sensitive'
    'USER1':'password123',
    'USER2':'secret123',
    'BAKEDBINARY':'Soop3rSecr3t',
    'USER3':'USER4',
}
def user_sanitizer(usernamell, authll, passwordll):
    """Cleans the input of the Username & password"""
    if(authll == "cliq"):
        print(f"\n[+] CAPTCHA CORRECT!\n")
        for item1 in active_users:
            userll = item1.upper()
            numa1 = usernamell.upper()
            # Comparing USERNAME to USERNAME
            if (userll == numa1):
                authll = usernamell.upper()
                return authll     
    else:
        print(f"\n[x] Auth Failed\n")
        exit(0)
        return 0
while(1):
    print(f" + Authorization + ")
    auth3 = input("$\tCODE # - > ")
    print(f" + USERNAME + ")
    user_input1 = input("$\t - > ")
    print(f" + PASSWORD + ")
    user_input2 = input("#\t - > ")
# Code -> auth3 | username - > user_input1 | password - > user_input2
    block1_Og = user_sanitizer(user_input1, auth3, user_input2)
    match1 = False
    if block1_Og in active_users:
        match1 = True
    if match1:
        print(f"\nWelcome back, {block1_Og.title()}\n")
        break
    else:
        print(f"[x] Failed")
if match1:
    for i in range(99):
        message1 = input("$\t# - > ")
        print(f"{message1}")
