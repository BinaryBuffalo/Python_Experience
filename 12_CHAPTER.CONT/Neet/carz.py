class Carz:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} Miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Odometer does not go down!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():

    def __init__(self, battery_size = 75):
        """Decribing the Battery size"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Describes the battery"""
        print(f"This car had a battery capasity of {self.battery_size}")
    def get_range(self):
        """Range of the battery"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"You can go about {range} miles on a full charge")

class ElectricCar(Carz):
    """Simple Electric Car Model in python"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class. 
            Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        