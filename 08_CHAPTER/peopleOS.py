my_list1 = []

for item in range(1,11):
    new_user = {
        'username':'bakedbinary',
        'first_name':'lee',
        'last_name':'lezlander',
        'banned':'no',
    }
    my_list1.append(new_user)
    lengthll = len(my_list1)


for item in my_list1:
    if item['banned'] == 'no':
        print(f"Welcome")
        banned = False
    else:
        print(f"Banned")
        banned = True
    if banned:
        print(f"Exit")
        exit(0)

    if item['username']:
        print(f"Username:   ->{item['username']}")
        
    if item['first_name']:
        print(f"First Name: ->{item['first_name']}")
    if item['last_name']:
        print(f"Last Name:  ->{item['last_name']}")