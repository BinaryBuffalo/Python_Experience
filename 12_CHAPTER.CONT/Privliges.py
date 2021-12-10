Users = ["slimy","ЭЭbakedbinary"]

match1 = False
isadmin = False	
ispublic = False

class Lego1:
	def __init__(self, unm):
		self.username = unm
	def great(self):
		print(f"Welcome Back! {self.username}")
	def admin(self):
		if self.username[0] == "Э" and self.username[1] == "Э":
			print(f"[!] ADMIN [!]~~~~~~[Welcome Back]")
			isadmin = True
#username Input
msg1 = input("USERNAME: ")


#
#Commands Add Them Here
# TYPE { Q } to kill
# ~~~~~~~~~~~~~~~~~~~~~~
def privs():
	if match1 == True and isadmin == True and ispublic == True:
		pass	
	else: 
		print("Forced Entery")
		exit(1)
	print("You are admin")
for items in Users:
	if items == msg1:
		# matched user
		saved_username = items
		match1 = True
		##
#checks to see if there was a matched user
if match1 == True:
	pass
else:
	exit(0)

#This saves the user settings
template1 = Lego1(saved_username)
#Greats The User By Default!
template1.great()
#Checks if The User is An Admin
template1.admin()

while(True):
	if match1 == False:
		print("Forced Entry")
		exit(0)
	command = input("$\t> ")
	if command == "privs -help":
		privs()