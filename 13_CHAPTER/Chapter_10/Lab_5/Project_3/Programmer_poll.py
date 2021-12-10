while True:
    print("Why Do you like programming?")
    msg1 = input("\t Reason ~> ")
    with open("POLL.txt", 'a') as f_obj1:
        cmdll = f"\n{msg1}"
        f_obj1.write(cmdll)