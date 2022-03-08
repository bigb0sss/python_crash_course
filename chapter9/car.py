class Car():

    def __init__(self, make, model, year):
        # Init atrributes
        self.make = make
        self.model = model
        self.year = year
        # Adding a dynamic attribute
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = "\n" + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("[ERROR] You cannot roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car("audi", "a4", 2016)

print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

# Modifying an attribute's value directly
my_new_car.odometer_reading = 25
my_new_car.read_odometer()

# Modifying an attribute's value through a method
my_new_car.update_odometer(24)
my_new_car.read_odometer()

# Incrementing an atrribute's value through a method
my_used_car = Car("BMW", "X5", 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23100)
my_used_car.read_odometer()

my_used_car.increment_odometer(200)
my_used_car.read_odometer()

