# Author: Baked Binary
# Creates a List & then copy's & prints both lists
my_list1 = ["Pizza", "Tacos", "Chili", "Worms"]
my_list2 = my_list1[:]
i=0
#Printing my list 1
for Items in my_list1:
    i += 1
    print(f"List Items : #{i} ({Items})")
#Printing my list 2
i=0
for Items2 in my_list2:
    i += 1
    print(f"\t\t\t\tList Items2 : #{i} ({Items2})")

