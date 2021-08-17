my_list1 = {
    'subaru': {
        'price':2000,
        'year':2003,
    },
    'toyoda':{
        'price': 7000,
        'year': 2005,
    },
     'ford':{
        'price': 9000,
        'year':2020,
    },
    'chevy':{
        'price': 30_000,
        'year': 2018,
    },
    'bmw':{
        'price': 5000,
        'year': 2009,
    },
}
cars = ['subaru', 'toyoda', 'ford', 'chevy', 'bmw']
for item in cars:
    print(f"\t{item.upper()},")
input1 = input("what Kind of Car would you like ?\n$   > ")
print(f"Searching for a {input1}\n")
for item in cars:
    if input1 in item:
        print(f"{input1.upper()} In stock now!")
for key, value1 in my_list1.items():
    pricell = value1['price']
    yearsll = value1['year']
    if input1.upper() == key.upper(): 
        print(f"\tWe have a {key} in stock for ${pricell} & brand new with a body \n\t Finish & model in {yearsll}")