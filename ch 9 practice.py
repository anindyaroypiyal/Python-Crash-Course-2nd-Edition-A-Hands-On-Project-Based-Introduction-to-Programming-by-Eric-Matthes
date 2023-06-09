"""from restaurant import Restaurant
r = Restaurant('cp','junk food')
r.describe_restaurant()
print()

import restaurant
r = restaurant.Restaurant('cp','junk food')
r.open_restaurant()
"""
from random import randint

class Die:
    """ properties of a die"""
    def __init__(self, sides=6):
        """ stores name and cuisine type of a restaurant """
        self.sides = sides

    def roll_die(self):
        print(f"You got {randint(1,self.sides)}")

dice6 = Die(6)
for c in range(5):
    dice6.roll_die()
print()
dice10 = Die(10)
for c in range(20):
    dice10.roll_die()
print()

from random import choice
tup = ('s','g',5,'f',7,'q','k',3,'v')
print("anyone having following combination is the lottery winner:")
for c in range(4):

    print(choice(tup), end = ' ')
