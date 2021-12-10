class car:

    def __init__(self, make, model, year):
        self.make  = make
        self.model = model
        self.year  = year
        self.orr   = 0
        self.life  = 0
    def get_name(self):
        details = f" MODEL | {self.model}\n MAKE  | {self.make}\n YEAR  | {self.year}"
        return details
    def set_miles(self, miles):
        if miles >= self.orr:
            self.orr = miles
        else:
            print("meter does not go back")
    def battery_life(self, perc):
        self.life = perc
        if self.life > 100:
            print("Enter A valid amount")
        elif self.life < 50:
            print("You need to change your battery!")
        else:
            print("Your battery is great!")

electric_car = car('Sports', 'Audi', 2016)
electric_car.orr = 53
print(electric_car.battery_life(80))
print(f" MILES | {electric_car.orr}")
