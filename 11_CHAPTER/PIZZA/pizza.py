def build_pizza(*toppings):
    """Builds pizza"""
    print("Toppings:")
    for top in toppings:
        zoo = top.split()
        for item in zoo:
            print(f" + {item}")
