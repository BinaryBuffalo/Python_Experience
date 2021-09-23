class rest:

    def __init__(self, res_name, cuisine_type, openornot):
        self.name = res_name
        self.type = cuisine_type
        self.time = openornot

    def desc(self):
        print(f"The name of your restaurant is {self.name}")
        print(f"The food styling of choice is {self.type}")
    def info(self):
        if self.time == True:
            t1m3 = "Open"
        else:
            t1m3 = "Closed"
        return t1m3 
msg1 = input("$ (resaurant name) ~> ")
msg2 = input("$ (cuisine type)   ~> ")
msg3 = input("$ (Current status) ~> ")
obj1 = rest(msg1, msg2, msg3)
obj1.desc()
obj1.info()