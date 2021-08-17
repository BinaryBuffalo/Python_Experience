import time
message1 = input("$ Number ~> ")
message1 = int(message1)

if message1 / 10:
    if (message1 % 10 == 0):
        print(f"\tWorking multiple of 10 --> input {message1}\n")
    else:
        print(f"\tNot a working multiple of 10 --> input {message1}")
