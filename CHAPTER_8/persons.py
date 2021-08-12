import time
my_list1 = {
    'person1': {
        'username':'coolman72',
        'name':'dan',
        'code': 5555,
               },    
    'person2':{
        'username':'dannanator',
        'name':'Birdperson',
        'code': 7782,
              },
    'person3':{
        'username':'TurkyPiano',
        'name':'wong',
        'code': 2782,
              },
            }        

print(f"\t\t\tRegisterd users -> \n")
for key, value in my_list1.items():
    print(f"\t\t\t[{key.upper()}] \n")
    time.sleep(1.0)

for keyl, valuel in my_list1.items():
    userll = valuel['username']
    codell = valuel['code']
    print(f"Username   ->  {userll}\nCode       ->  {codell}\n")
time.sleep(1)
for item, valuell in my_list1.items():
    namell = valuell['name']
    userlll = valuell['username']
    codelll = valuell['code']
    print(f"\t[username] | {userlll}")
    print(f"[ID]       | {item.upper()}")
    print(f"[name]     | {namell}")
    print(f"[code]     | {codelll}\n")
    time.sleep(2)
