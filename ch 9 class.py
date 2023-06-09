#-------------------------------------------------------------------------------

class Car:
 """A simple attempt to represent a car."""
 def __init__(self, make, model, year):
     self.make = make
     self.model = model
     self.year = year
     self.odometer_reading = 0

 def get_descriptive_name(self):
     long_name = f"{self.year} {self.manufacturer} {self.model}"
     return long_name.title()

 def read_odometer(self):
     print(f"This car has {self.odometer_reading} miles on it.")

 def update_odometer(self, mileage):
     if mileage >= self.odometer_reading:
         self.odometer_reading = mileage
     else:
        print("You can't roll back an odometer!")

 def increment_odometer(self, miles):
     self.odometer_reading += miles

#-------------------------------------------------------------------------------

class Restaurant:
    """ model of a Restaurant """
    def __init__(self, restaurant_name, cuisine_type):
        """ stores name and cuisine type of a restaurant """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is a very popular restaurant")
        print(f"This restaurant severs {self.cuisine_type.title()} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open 24x7 from 10AM to 11PM.")

    def set_number_served(self,s):
        if (s >= self.number_served):
            self.number_served = s
        else:
            print("changes are not acceptable")

    def increment_number_served():
        if (s >= self.number_served):
            self.number_served += s


favorite_restaurant = Restaurant('chillox','fast food')
print(f"My favorite restaurant is {favorite_restaurant.restaurant_name} and it is a {favorite_restaurant.cuisine_type} restaurant ")
favorite_restaurant.open_restaurant()
a = Restaurant('Rainbow','Multi cuisine')
print(f"\nMy favorite restaurant is {a.restaurant_name} and it is a {a.cuisine_type} restaurant ")
a.open_restaurant()

a.describe_restaurant()
print()

b = Restaurant('dc','chinese')
b.describe_restaurant()
print()

s = Restaurant('sultan','kacchi')
s.describe_restaurant()
print(f"NO. of people served {s.number_served}")
s.set_number_served(5)
print(f"NO. of people served {s.number_served}")
print()

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'butterscotch', 'almond']

    def flav(self):
        print(f"{self.restaurant_name.title()} has the following ice-cream flavors: ")
        for flavor in self.flavors:
            print(f"-{flavor}")


ice1 = IceCreamStand('iceland','ice cream stand')

ice1.open_restaurant()

ice1.flav()
