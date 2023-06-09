""" print("hello py")

name = input("write your name: ")
print(f"\nHello {name}")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
prompt += "\ncome on.. "
name = input(prompt)
print(f"\nHello, {name}!")

            #type casting

age = input("tell us your age: ")
age = int(age)

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print(f"\nThe number {number} is even.")
else:
 print(f"\nThe number {number} is odd.")

print()


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""    #python has to compare with something, in this case it's an empty string.
while message != 'quit':
 message = input(prompt)

 if message != 'quit':
 print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


#break, continue, infinite loop (we know these)

"""

unverified_users = ['porosh','rohan','fujiwara']
confirmed_users = []

while unverified_users:
    currentUser = unverified_users.pop()
    print(f"Verifying {currentUser.title()}!")

    confirmed_users.append(currentUser)
print()

for user in confirmed_users:
    print(f"{user.title()} is confirmed.")
print()


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)
