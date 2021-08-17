import time
unconfirmed_users = ['dan', 'pam', 'joey']
confirmed_users = []

while(unconfirmed_users):
    current_users = unconfirmed_users.pop()
    print(f"\tVerify users - - -> {current_users}")
    confirmed_users.append(current_users)
print(f"\n\t+ Verfied users +")
print(f"\t[+]===================[+]")
for items in confirmed_users:
    print(f"\t\tUser#1 {items}")
print(f"\t[+]===================[+]")

pets = ['cow','cat','cat','cat','dog','mouse']
print(f"\nCurrent pets")
print(f"[+]===================[+]")
for item in pets:
    print(f"{item}")
print(f"[+]===================[+]")
print("Removing cats")
while 'cat' in pets:
    pets.remove('cat')
time.sleep(2)

print(f"\nCurrent2 pets")
print(f"[+]===================[+]")
for item in pets:
    print(f"{item}")
print(f"[+]===================[+]")




