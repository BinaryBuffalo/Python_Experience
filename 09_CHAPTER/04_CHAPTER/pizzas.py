#   Author: BakedBinary
#   creates 1 List & copy's it then Shows Items in both lists   
i = 0
my_list1 = ["cheese", "vegan", "pepperoni"]
my_list2 = my_list1[:]
print(f"My Favorite Food    : {my_list1}")
print(f"My Friends Favorite : {my_list2}")
my_list1.append('BBQ')
my_list2.append('Hawain')
print(f"\n\tMy Favorite Food    : {my_list1}")
for Items in my_list1:
    i += 1
    print(f"\t\t\t\tFood Item: #{i} -> {Items}")
