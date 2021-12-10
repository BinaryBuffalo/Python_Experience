filename = input("\tFile Name ~> ")
#read the file content line by line
with open(filename) as file_obj1:
    for line in file_obj1:
        print(line)

#reads & saves file contents then print the line from pointer
with open(filename) as file_obj2:
    lines = file_obj2.readlines()
for line in lines:
    print(line)