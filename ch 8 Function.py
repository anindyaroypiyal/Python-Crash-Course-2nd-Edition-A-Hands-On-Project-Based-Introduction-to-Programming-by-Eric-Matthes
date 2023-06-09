def greet_user(username):
    """ greeting user""" #This is called a docstring
    print(f"Hello, {username.title()} !")

greet_user('roy')

def recent_book(bookname):
    print(f"I recently read the book named \"{bookname.title()}\"")

recent_book('the richest man in babylon')
print()

def make_shirt(text, size=38):
    print(f"\nYou have ordered a t-shirt of size: {size}")
    print(f"The text on your t will be: {text}")

make_shirt(text = 'Step UP!', size = 40) #keyword argument
make_shirt('Shut UP!',42)   #positional argument
make_shirt('whodunnit ?')   #default argument
print()

def format_name(firstName, lastName, middleName = ''):
    if middleName:
        full = f"{firstName} {middleName} {lastName}"
    else:
        full = f"{firstName} {lastName}"
    return full.title()
person = format_name('anindya', 'roy', 'piyal')
print(person)

"""
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

 f_name = input("First name: ")
 if f_name == 'q':
     break

 l_name = input("Last name: ")
 if l_name == 'q':
     break

 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!")
"""
print()
def city_country(country,city):
     str = f"{city},{country}"
     return str

a = city_country(city = 'Santiago', country = 'Chile')
b = city_country(city = 'Brooklyn', country = 'USA')
print(a)
print(b)
print()

def make_album(artist_name, album_title, song_count=None):
    album = {'Artist Name': artist_name.title(),'Album': album_title.title()}
    if song_count:
        album['NO. of Songs'] = song_count
    return album

a = make_album('lisa henigan', 'passenger' )
b = make_album(album_title = 'after hours' , artist_name = 'the weeknd', song_count = 13)
print(a)
print(b)
print()

"""
while True:
    name = input("\nWhat is the artist's name ?(press 'q' to close program): ")
    if name == 'q':
        break
    title = input("What is the album title ?(press 'q' to close program): ")
    if title == 'q':
        break
    al = make_album(name,title)
    print("Album info: ",al)
"""
def show_message(messages):
    for message in messages:
        print(message)

def send_message(messages):
    while messages:
        copy = messages.pop()
        print("from send_message:::",copy)
        sent_messages.append(copy)


Messages = ['hello','ssup','no','busy now']
show_message(Messages)
sent_messages = []
print()
print("messages:",Messages)
print("sent :",sent_messages)
print()
send_message(Messages)
print("\nmessages:",Messages)
print("sent :",sent_messages)

def make_pizza(*toppings):
 """Summarize the pizza we are about to make."""
 print("\nMaking a pizza with the following toppings:")
 for topping in toppings:
     print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
 """Summarize the pizza we are about to make."""
 print(f"\nMaking a {size}-inch pizza with the following toppings:")
 for topping in toppings:
     print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def prep_sandwich(*items):              # *means tupple
    print("\nYou have the following items in your sandwich: ")
    for item in items:
        print(f"-{item}")

prep_sandwich('cheese','sause','latuce')    #practice 8-12
print()


def build_profile(first, last, **other_info):               # **means empty dictionary
    other_info['First Name'] = first.title()
    other_info['Last Name'] = last.title()
    return other_info

user1 = build_profile('anindya','roy',University = 'BRACU', ID = 19101577, Batch = 'Spring 2019')
print('We have the following info about this user:')
for k,v in user1.items():
    print(f"{k}: {v}")

#Importing module in python program. Import functions from other files. must end with .py ; an example below.

""" import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza as mp (as = alias)
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') """
