#Author: Baked Binary
#Python 3.6 
# Dictinory of names & nums Which gets printed multiple types
fav_num = { 
    'name1': 'tom', 'num1': -5,
    'name2': 'jared', 'num2': 84,
    'name3': 'payton', 'num3': 1002,
    'name4': 'tyler', 'num4': 103,
    'name5': 'dan', 'num5': 7,
    }
#fav_num = { 
#    'tom'   : -5,
#    'jared' : 84,
#    'payton': 1002,
#    'tyler' : 103,
#    'dan'   : 7,
#    }


#This is horrible in Every Way
print(f"{fav_num['name1']}'s Favorite number is {fav_num['num1']}")
print(f"{fav_num['name2']}'s Favorite number is {fav_num['num2']}")
print(f"{fav_num['name3']}'s Favorite number is {fav_num['num3']}")
print(f"{fav_num['name4']}'s Favorite number is {fav_num['num4']}")
print(f"{fav_num['name5']}'s Favorite number is {fav_num['num5']}")

#for key, valuel in fav_num.items():
#    print(f"{key}'s Favorite numbers {valuel} ")