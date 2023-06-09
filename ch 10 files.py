""" with open('learning_python.txt') as file_object:
    content = file_object.read()
    print(content)
print()
with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
print()
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.replace('Python','C').strip())
print()

while True:
    user = input('Your name please (press q to exit): ')
    if user == 'q':
        break
    print(f"Hello {user}, Welcome.")
    with open('guest_book.txt', 'a') as file_object:
        entry = f"\n{user} has registered"
        file_object.write(entry)

with open('guest_book.txt') as file:
    content = file.read()
    print(f"\nHere is the guest list:\n{content}")

while True:
    #addition
    print("i will add 2 numbers.\n")
    num1 = input('Please enter 1st number (press q to exit): ')
    if num1 == 'q':
        break
    num2 = input('Please enter 2nd number (press q to exit): ')
    if num2 == 'q':
        break
    try:
        add = int(num1) + int(num2)
    except ValueError:
        print('Sorry you cannot add letters')
    else:
        print(add)


import json

fav_num = input("If you tell me your favourite number, i'll remember it forever..  ")
filename = 'favourite.json'
with open(filename, 'w') as f:
    json.dump(fav_num, f)

filename = 'favourite.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    print("sorry you haven't told us the number yet.")
else:
    print(f"So, your favorite number is {number}. Right ?")
"""

import json

filename = 'favorite.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    print("you haven't told us your favourite number before, tell us now and we'll remember forever.. ")
    fav_num = input()
    filename = 'favourite.json'
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
        print("We'll remember when you ask next time.")
else:
    print(f"So, your favorite number is {number}. Right ?")
