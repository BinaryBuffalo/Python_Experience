import time
my_list1 = {}
def active_rooms():
	"""Prints list of current rooms"""
	for key1, value1 in my_list1.items():
		print(f"{key1}, -> {value1}")
pase = True
while(pase):
	active_rooms()
	print(f"\n\t[1] booked\n\t[2] free\n")
	message = input("$\t# - > ")
	if(message == '1'):
		room = "booked"
	elif(message == '2'):
		room = "free"
	else:
			print(f"Option failed")
			exit(0)
	print(f"\nWhat is room number #\n")
	message = input("$\t# - > ")
	message = f"room{message}"
	my_list1[message] = room