class car:
    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year
        self.orr    = 0
    def get_name(self):
        details = f" MODEL | {self.model}\n MAKE  | {self.make}\n YEAR  | {self.year}"
        return details
    def set_miles(self, miles):
        if miles >= self.orr:
            self.orr = miles
        else:
            print("meter does not go back")

car1 = car('Sports', 'Audi', 2016)
print(car1.get_name())
car1.orr = 53
print(f" MILES | {car1.orr}")
