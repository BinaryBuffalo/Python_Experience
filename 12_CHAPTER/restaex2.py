class rest:
    def __init__(self, res_name, cuisine_type, openornot):
        """takes in |name|->var |cuisine|->var |open or close|->Bool"""
        self.name = res_name
        self.type = cuisine_type
        self.time = openornot

    def desc(self):
        """In the other examples this is 2 lines long now its 1 :)"""
        print(f"{self.name} is currently serving {self.type}")
    def info(self):
        """prints the name & status after checking | self.time | """
        if self.time == True:
            t1m3 = "Open"
        else:
            t1m3 = "Closed"
        print(f"{self.name} is {t1m3}") 

rest1 = rest("Pizza pal-ice", "pizza", True)
rest1.info()
rest1 = rest("chessinos", "pizza",  False)
rest1.info()
rest1 = rest("chucky-cheese", "butthole",  True)
rest1.desc()
# hehehehhehe chucky cheese is greasy