message1 = input("How many people are sitting at the table -> ")
message1 = int(message1)
if (message1 <= 8):
    print(f"Please, take a seet\n")
else:
    print(f"You have to wait for a table\n")