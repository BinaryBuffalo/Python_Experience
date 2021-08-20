names = {}
i = 0
def nmss():
	"""Prints current poll"""
	print("\n")
	for key, value in names.items():
		print(f"\t|{key}| ---> |{value}")
while(1):
	nmss()
	print(f"\n[add] or [remove]\n")
	pok1 = False
	pok2 = False
	input1 = input("$\t# - > ")
	if(input1 == "add"):
		pok1 = True
	if(input1 == "remove"):
		pok2 = True
	if(pok1):
		i += 1
		slot = f"name{i}"
		print("\n\tWhat is your name\n")
		message = input("$\t# - > ")
		names[slot] = message
		print(f"Added {message} to list...")
	if(pok2):
		nmss()
		print(f"\nRemove name ?\n")
		message = input("$\t# - > ")
		names.pop(message)
		print(f"attempted to remove {message}")




