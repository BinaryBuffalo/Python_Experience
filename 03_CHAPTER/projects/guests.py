guests = ["Snoop", '69', "Drake"]
print("The people who are invited are ")
#Creating a list & removing 1 
print(f"{guests[0]}\t{guests[1]}\t{guests[2]}\n")
print(f"It's too bad but '{guests[1]}' Can't make it")
del guests[1]
guests.append('PoloG')
print(guests)
print("\nI just got a bigger dinner tables Invite 3 more guests")
#inserting Nicky to front & jack to middle, then adding peter
guests.insert(0, 'Nicky')
guests.insert(2, 'Jack')
guests.append('Peter')
print(guests)
print("Mom said only 2 guests")
# Adding names to the not invited list
# note: Must to backwords so that way you dont change
#       The front of the list.
not_inv4 = guests.pop(5)
not_inv3 = guests.pop(3)
not_inv2 = guests.pop(2)
not_inv1 = guests.pop(0)
print(f"Not Invited -> {not_inv1}, {not_inv2}, {not_inv3}, {not_inv4}")
print(f"\nInvited     -> {guests[0]}, {guests[1]}")