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
