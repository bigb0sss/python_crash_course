class Dog():
    # Class to model a dog

    # __init__ method is a special Python method is that it runs automatically
    def __init__(self, name, age):
        # Initializing name and age attributes
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

# How to use Class --> Simple example
my_dog = Dog('willie', 6)

print("My dog name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Calling Class methods
my_dog.sit()
my_dog.roll_over()