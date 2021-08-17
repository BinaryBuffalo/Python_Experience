import time
my_list1 = {
    'pet1':{
        'breed':'black lab',
        'owners name': 'Spongboobman',
        'age': 7,
        'name':'leroy',
        'shots': True,
           },
    'pet2':{
        'breed':'white lab',
        'owners name': 'MrSmartyPants',
        'age': 2,
        'name':'james',
        'shots': True,
           },
    'pet3':{
        'breed':'bulldog',
        'owners name': 'Babysmeller22',
        'age': 2,
        'name':'ricky',
        'shots': True,
           },
    'pet4':{
        'breed':'poodle',
        'owners name': 'DickJamkok',
        'age': 2,
        'name':'micky',
        'shots': True,
           },
        }

for key, value in my_list1.items():
    breedll = value['breed']
    onamell = value['owners name']
    agell = value['age']
    namell = value['name']
    shots = value['shots']
    print(f"[{onamell}] You own the [{breedll}]")
    time.sleep(0.2)
    if shots == False:
        print("You need to pay for shots\n +100")
        exit(0)
    else:
        print("Shots [Complete]")
    print(f"Dog Age is {agell}yrs old")
    if agell > 13:
        print(f"health checkout soon? {namell}")
    else:
        print(f"You want a cookie {namell}?\n")
time.sleep(0.2)

    
