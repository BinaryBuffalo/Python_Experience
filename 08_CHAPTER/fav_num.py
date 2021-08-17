my_list1 = {
    'A1':{
        'name':'tommy',
        'number': 8,
         },
    'A2':{
        'name':'danny',
        'number': 5,
         },
    'A3':{
        'name':'connor',
        'number': 807,
        },
    'A4':{
        'name':'teddy',
        'number': 1007,
        },
    'A5':{
        'name':'connor',
        'number': 6,
        },
       }

for item1, value1 in my_list1.items():
    namell = value1['name']
    numberll = value1['number']
    print(f"Hello {namell}, Your Favorite number is {numberll}")