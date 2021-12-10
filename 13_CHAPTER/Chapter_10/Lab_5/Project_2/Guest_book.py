login_attempts = 0
while True:
    username = input("\tUSERNAME: ")
    authtokn = input("\tTOKEN   : ")
    #Log The username
    print(f"Attemping sign in {username}")
    with open("LOGS.txt", 'a') as f_obj1:
        cmdll = f"\nusername -> {username}\nTOKEN -> {authtokn}"
        f_obj1.write(cmdll)
    if authtokn == "SECRETPASSCODE123":
        print("[!] Login Succesfull")
        pass
    else:
        print("[x] Authorization code Incorrect")
        login_attempts += 1
        if login_attempts == 3:
            print("You've Failed 3 Login Attempts")
            exit(0)
        pass
    