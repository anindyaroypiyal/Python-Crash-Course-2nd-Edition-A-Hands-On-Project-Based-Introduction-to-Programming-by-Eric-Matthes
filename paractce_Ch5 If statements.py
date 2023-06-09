cars = ['audi','lambo','toyota','bmw','tesla']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'AUdi'
print("car=",car.lower() == 'audi')

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("topping=",'onions' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can comment if you wish")

age = 19
if (age >= 18):
    print("you're allowed to vote")


                    #Allien color
alien_clr = 'green'
if alien_clr == 'red':
    print("player got 5 points")
elif alien_clr == 'yellow':
    print("player got 1 points")
else:
    print("player got no point\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping == 'green peppers':
     print("Sorry, we are out of green peppers right now.")
 else:
     print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = ['onions']
if requested_toppings:
    for req_top in requested_toppings:
        print(f"Adding {req_top} in your pizza")
    print(f"\nFinished making your pizza!")
else:
    print("you sure you want plain pizza ?")
