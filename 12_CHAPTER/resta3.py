class rest:

    def __init__(self, res_name, cuisine_type, openornot):
        self.name = res_name
        self.type = cuisine_type
        self.time = openornot

    def desc(self):
        print(f"\nThe name of your restaurant is {self.name}")
        print(f"The food styling of choice is {self.type}\n")
    def info(self):
        if self.time == True:
            t1m3 = "Open"
        else:
            t1m3 = "Closed"
        return t1m3 

while True:
    msg1 = input("\n$ (resaurant name) ~> ")
    msg2 = input("$ (cuisine type)   ~> ")
    msg3 = input("$ (Current status) ~> ")
    obj1 = rest(msg1, msg2, msg3)
    obj1.desc()
    obll = obj1.info()
    if obll:
        print(f"///////////////////////////\n// {obj1.name} is {obll}  //\n///////////////////////////")