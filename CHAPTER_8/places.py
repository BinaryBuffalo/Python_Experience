my_list1 = {
    'luke wizardman': {
        'USA':'New York',
        'France':'Paris',
        'Romania':'Sibiu',
        'England':'Canada', 
            },
    'Brian':{
        'Mexico':'Australia',
        'Singapore':'England',
        'Russia':'China',
        'Ukrain':'Japan',
             },
       'Pam':{
        'Ukrain':'Russia',
        'China':'Germany',
        'Italy':'Turkey',
             },
            }

for key, value in my_list1.items():
    namell = key.upper()
    print(f"Welcome Back {key.upper()}")
    print(f"{key}'s Top Favorite places are \n")
    print(f"[{namell}] -> {value}.\n")