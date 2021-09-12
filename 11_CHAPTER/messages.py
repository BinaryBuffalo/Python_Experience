messages = []
sent_messages = []
while 1:
    print("[+] Option : ")
    print("\t[1] add message to a list")
    print("\t[2] print messages")
    print("\t[3] send messages")
    print("\t[4] save messages")
    message1 = input("$\t> ")
    if message1 == '1':
        print("What message would you like to add")
        usrput = input('$\t~> ')
        messages.append(usrput)
    if message1 == '2':
        i = 0
        print("[+]==============================[+]")
        for mesall in sent_messages:
            i += 1
            msg = f"Message #{i} | {mesall}"
            print(msg)
        print("[+]==============================[+]")
    if message1 == '3':
        while messages:
            curdes = messages.pop()
            sent_messages.append(curdes)
    if message1 == '4':
            f = open("archive.txt", "w")
            for jj in sent_messages:    
                cmd1 = f"{jj}\n"
                f.write(cmd1)
            f.close()
