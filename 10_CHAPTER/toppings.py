toppings = {
    'pizza toppings':{
        'top1':['mushrooms','cheese'],
        'top2':['pepperoni','bacon'],
                    },
    'fry topppings': {
        'top1':['ketchup','mustard'],
        'top2':['mayo','relish'],
                     },
            }
print(f"Toppings")
current_toppings = []

print(f"[+]=================[+]")
                            ##
for key, valuel in toppings.items():
    print(f"{key}")
    obj_1 = valuel['top1']
    obj_2 = valuel['top2']
    for item in obj_1:
        print(f"{item}")
        ##
    for item2 in obj_2:
        print(f"{item2}")
        ##
    print(f"[+]=================[+]")
    ##
    for key1, value2 in toppings.items():
        print("\nWhat topping would you like to add")
        message1 = input("$ Toppings ~> ")
        top3 = value2['top1']
        top4 = value2['top2']
        if message1 in top3:
            print(f"Adding --> [{message1}]")
            current_toppings.append(message1)
        ##
        elif message1 in top4:
            print(f"Match --> [{message1}]")
            current_toppings.append(message1)
        else:
            print(f"Failed to add {message1}")
    