alien_0 = {'color': 'blue', 'point': 3}
print(alien_0['color'],end = '  ')
print(alien_0['point'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#start with empty dictionary

alien_0 = {}
alien_0['color'] = 'green'
alien_0['score'] = 3
print(alien_0)
alien_0['color'] = 'red'
print(f"After alien is shot it is now {alien_0['color']}")
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
 # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

id = {'rohan': 1, 'porosh': 3, 'someone': 8}
print(id)
del id['someone']
print(id)

favourite_languages = {
    'a' : 'python',
    'b' : 'java',
    'c' : 'c#',
    'd' : 'html'
    }
print(favourite_languages)

language = favourite_languages['c'].title()
print(f"Their favourite lang is {language}")

print(favourite_languages.get('e', "can't find it !"))
print()

for k,v in favourite_languages.items():
    print(f"name = {k.title()} ; favourite language = {v.title()}\n")

for key in favourite_languages.keys():
    print(key)

friends = {'r', 'd', 'a'}
for name in favourite_languages.keys():
    print("hi ",name.title())

    if name in friends:
        language = favourite_languages[name].title()
        print(f" well, the favourite language of {name.title()} is, {language}")


phones = {'piyal': 'xiaomi', 'porosh': 'iPhone', 'fujiwara': 'realme', 'hisam': 'nokia', 'rohan': 'xiaomi'}
for key, val in sorted(phones.items()):
    print(f"{key.title()} uses {val.title()}.")

print('We only have these phones in showroom:', end = ' ')
for val in sorted(set(phones.values())):
    print(val, end = '  ')

print()

                            #We're going deeper in the ocean; Nesting

alien_0 = {'color' : 'green', 'speed' : 'slow', 'point' : 5}
alien_1 = {'color' : 'yellow', 'speed' : 'medium', 'point' : 10}
alien_2 = {'color' : 'red', 'speed' : 'fast', 'point' : 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print()

aliens = []
for alien in range(20):
    new_alien = {'color' : 'green', 'speed' : 'slow', 'point' : 5}
    aliens.append(new_alien)
for alien in aliens[:3]:
    print(alien)
print('...',end = '\n\n')

for alien in aliens[:2]:
    if (alien['color'] == 'green'):
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif (alien['color'] == 'yellow'):
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15


for alien in aliens[:6]:
    print(alien)
print()

for alien in aliens[:2]:
    if (alien['color'] == 'green'):
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['point'] = 10
    elif (alien['color'] == 'yellow'):
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['point'] = 15

for alien in aliens[:4]:
    print(alien)

pizza = {'crust' : 'thicc',
        'toppings' : ['sausage','extra cheese']
        }
print(f"You ordered a {pizza['crust']}- crust pizza"
    "with following topings:")
for topping in pizza['toppings']:
    print("\t"+topping)

favorite_languages = { 'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
 }
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

users = {
 'aeinstein': {
 'first': 'albert',
'last': 'einstein',
 'location': 'princeton',
 },

 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
