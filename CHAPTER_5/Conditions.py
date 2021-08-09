#   Author: BakedBinary
my_list1 = ['subaru', 'bmw']
num_list = (18, 21, 17, 22)
#test1
print("list[1] == 'bmw'\nPrediction True ")
print(my_list1[1] == 'bmw')
#test2
print("list[0] == 'bmw'\nPreditction False")
print(my_list1[0] == 'bmw')
#test3
my_list2 = ["foo", "bar", "baz", "taz", "zaz"]
username = "daddy"
bogg = False
if username not in my_list2:
    bogg = True
print(f"Username Valid {bogg}")
#test4
bogg2 = False
if num_list[0] >= 21:
    bogg2 = True
print(num_list)
print(f"is #1 <= 21 {bogg2}")
#test5
my_list3 = ["NUTLICKER", "nutL1ck3r", "nutliqour"]
nameuser = "nutlicker"
bogg3 = False
if nameuser.lower() == my_list3[0].lower():
    bogg3 = True
print(f"Username taken? -> {bogg3}")





