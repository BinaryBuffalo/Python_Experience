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
    User1 = Users(msg1, msg2)
    User1.greet()