dogs = ['husky','rotwhiler', 'shepherd', 'shiba inu']
#for dog in dogs:
#    print(dog)

for dog in dogs:
    print(f"{dog.title()}'s are loyal\n")

for value in range(6):
    print(value)
print()

for value in range(2,8):
    print(value)
print()

for value in range(11,1,-2):
    print(value)             #odd numbers
print()

odd = list(range(1,11,2))
print(f"List of odd numbers <10: {odd}")

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares,"\n")
print("min =",min(squares))
print("max =",max(squares))
print("sum =",sum(squares))
print()

Squares = [val**2 for val in range(1,11)]              #shorter form, it's called List Comprehension
print(Squares)

""" million = list(range(1000001))
for value in million:
    print(value)
print("max = ",max(million))
print("sum = ",sum(million)) """

                        #part of a List
Names = ['rohan','rifat','porosh','fujiwara']
print(Names[1:3])
print(Names[:3])
print(Names[:])
print(Names[0:4:2])
print(Names[:-3])

print("last 3 names are:")
for name in Names[-3:]:
    print(name,"\n")                 #slice of a List

                    #copy of a List

my_fav_foods = ['pizza','pasta','chana','chicken','fried rice']
friend_fav = my_fav_foods[:]
my_fav_foods.insert(2,'soup')
friend_fav.append('chowmein')
print("mine are:",my_fav_foods)
print("his are:",friend_fav)

for val in range(5,11):
    print(val,"L",sep='&',end= ' ')        #print() parametarization
print()

                    #Tupples(Lists that can't be modified)

dimentions = (100,40)
for dime in dimentions:
    print(dime)
print(dimentions)

m_t = (4,)
print(m_t)
