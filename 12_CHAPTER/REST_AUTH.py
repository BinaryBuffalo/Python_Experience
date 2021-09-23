active_users = {
    'USER1':'password123',
    'USER2':'secret123',
}
def problem_to_log():
    print("[x] Authentication Error")
    exit(0)

def user_sanitizer(usernamell, passwordll):
    #loops through usernames in a dictionary
    for item1 in active_users:
        userll = item1 #save the username 
        auth = "one" #Default auth 
        #capitalize the USERNAME from the dictionary & userinput
        if(userll.upper() == ui1):
                namell = userll.upper()
                auth = namell
                return auth
    return auth
    
class rest:

    def __init__(self, name, type, open):
        self.name = name
        self.type = type
        self.time = open
        self.customer = 0

    def desc(self):
        print(f"The name of your restaurant is {self.name}")
        print(f"The food styling of choice is {self.type}")

    def info(self):
        if self.time == "open":
            t1m3 = "open"
        else:
            t1m3 = "closed"
        return t1m3 

    def add_uu(self, amt):
        if amt >= self.customer:
            self.customer += amt
            return self.customer
        else:
            print("[x] Failed ")
match1 = False
match2 = False
print("\t[+]==============[+]")
print("\t| | Welcome  To  | |")
print("\t| |  food guru   | |")
print("\t[+]==============[+]\n\n")
print("\t + USERNAME + ")
user_input1 = input("$\t - > ")
ui1 = user_input1.upper()
print("\t + PASSWORD + ")
user_input2 = input("#\t - > ")






block1_Og = user_sanitizer(user_input1, user_input2)
binn1 = "HoolaHoop"
if block1_Og == "one":
    problem_to_log()
else:
    binn1 = ui1
if(block1_Og == binn1):
    #checks the username
    match1 = True
    #if match1 is True
    if(match1 != False):
                #active_users['username']
        passwrd1 = active_users[binn1]
        if(user_input2 == passwrd1):
            match2 = True
else:
    problem_to_log()

if match2 == True:
    print(f"Welcome back {ui1.title()}")
else:
    problem_to_log()

msg1 = input("$ (resaurant name) ~> ")
msg2 = input("$ (cuisine type)   ~> ")
msg3 = input("$ (Current status) ~> ")
obj1 = rest(msg1, msg2, msg3)
while True:
    obj1.desc()
    status = obj1.info()
    print("How many Customers did we have today")
    mhh = input("$\t~> ")
    people = obj1.add_uu(int(mhh))
    print(f"Total Customers | {people}")
    print(f"Store STATUS    | {status}")