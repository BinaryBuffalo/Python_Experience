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