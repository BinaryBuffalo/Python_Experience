toppings1 = []
print("What would you like on your samwich")
print("[+] Type 'done' when finished")
cmd1 = "$\t~> "
k = 1
while k:  
    msgl1 = input(cmd1) 
    if(msgl1 == 'done'):
        k = 0
    else:
        toppings1.append(msgl1)
if k == 0:
    print(f"Adding These toppings to the pizza\n")
    for items in toppings1:
        ms1 = f"\t{items}"
        print(ms1)




