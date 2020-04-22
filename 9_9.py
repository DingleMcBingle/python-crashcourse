class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwH battery.")

    def get_range(self):
        """print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrades the battery of the car"""
        if self.battery_size <= 85:
            self.battery_size = 85
            print("Battery upgraded to 85 kwH.")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla','model s', 2016 )
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()