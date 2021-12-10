class icecream:
    def __init__(self, res_name, openornot):
        self.name = res_name
        self.time = openornot

    def desc(self):
        print(f"\tIcecream Truck name ~> {self.name}")

    def flavors(self):
        print("\t\t[Flavors]")
        print("\t\t      1.   Chocolate")
        print("\t\t      2.   Vinilla")
        print("\t\t      3.   Strawberry\n")
        print("\t\t\n")

def info(status):
    if status == "open" or status == "Open":
        t1m3 = "Open"
    else:
        t1m3 = "Closed"
    return t1m3 

msg1 = input("$ (Cream Truck name)            ~> ")
msg2 = input("$ (Open or Closed)              ~> ")
print("\n\n")
template1 = icecream(msg1, msg2)
template1.flavors()
template1.desc()
obj1 = info(msg2)
print(f"\tCurrent Status: {obj1}\n")
