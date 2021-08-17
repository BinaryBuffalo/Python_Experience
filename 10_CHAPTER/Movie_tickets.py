while(1):
    message1 = input("What is your Age\n$ Option ~> ")
    nummes1 = int(message1)
    for num in range(1, 99):
        if(nummes1 <= 3):
            print(f"FREE pass\n")
            break
        if(nummes1 >= 16):
            print(f"Tickes $15\n")
            break
        elif(nummes1 <= 15):
            print(f"Tickets $10\n")
            break
        else:
            print(f"Tickets 15$\n")

