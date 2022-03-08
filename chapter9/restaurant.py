class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descritbe_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " makes good " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is OPEN!")

class User():

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    # method
    def describe_user(self):
        print("User's name is " + self.first_name.title() + " " + self.last_name.title() + ".")
        print("User's age is " + str(self.age) + ".")
        print("User's gender is " + self.gender + ".")

    def greet_user(self):
        print("Hello " + self.first_name.title() + "!")

# instances
my_restaurant = Restaurant('Pizzaria', "Hoggie")

my_restaurant.descritbe_restaurant()
my_restaurant.open_restaurant()

my_user = User("Ryan", "Vola", 15, "Male")

my_user.describe_user()
my_user.greet_user()