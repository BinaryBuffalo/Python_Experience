filename = input("\tFile Name ~> ")

with open(filename, 'w') as file_obj1:
    file_obj1.write("Hello\nWorld!\n")
with open(filename, 'a') as file_obj2:
    file_obj2.write("I love programming!")