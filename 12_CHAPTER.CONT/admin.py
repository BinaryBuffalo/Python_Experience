class Admin:
    def __init__(self, usrnm, passwd):
        self.username = usrnm
        self.password = passwd
    def great(self):
        print("Hello, admin: Welcome Back")
        print("Last sign in date was -> (N/A)")

class Users:

    def __init__(self, username, password):
        self.usrnme = username
        self.passwd = password
    def greet(self):
        print(f"Hello {self.usrnme}, Welcome back!")
        print(f"Your password is {self.passwd}")
 
while(1):
    msg1 = input("$ (username) ~> ")
    msg2 = input("$ (password) ~> ")
    if msg1 == 'admin':
        temp1 = Admin(msg1, msg2)
        temp1.great()
    else:
        User1 = Users(msg1, msg2)
        User1.greet()