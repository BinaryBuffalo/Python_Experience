#   Author: BakedBinary
age = input("What is your age -> ")
if age < 2 and age > 0:
    print("You are a Baby")
elif age >= 2 and age <= 4:
    print("You are a Toddler")
elif age >= 5 and age <= 12:
    print("You are a Kid")
elif age >= 13 and age <= 19:
    print("you are a Teenager")
elif age >= 20 and age <= 64:
    print("you are a Adult")
elif age >= 65 and age <= 112 or age == 65:
    print("you are a Senior Citizen")
elif age >= 112:
    print("you are not alive")
else:
    print("You are still a sperm")
