class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65-kWh.")
        else:
            print("Battery already upgraded.")

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

my_tesla = ElectricCar('Dodge', 'Charger', 2023)
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()