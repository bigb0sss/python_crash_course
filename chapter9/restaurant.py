class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descritbe_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " makes good " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name.title() + " is OPEN!")

my_restaurant = Restaurant('Pizzaria', "Hoggie")

my_restaurant.descritbe_restaurant()
my_restaurant.open_restaurant()