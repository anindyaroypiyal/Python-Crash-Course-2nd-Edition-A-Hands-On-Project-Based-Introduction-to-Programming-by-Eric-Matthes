alphabets = ['a', 'b' , 'c', 'd', 'e']
print(alphabets, "\n")
print(alphabets[3], "\n")

vehicles = ['car', 'bike', 'bicycle', 'bus']
message = f"I like to travel by {vehicles[0].title()} & by {vehicles[-1].title()}"
print(message)

motorcycles = ['honda', 'ktm', 'yamaha', 'harley']
print(motorcycles)
motorcycles[2] = 'dune'
print(motorcycles)

motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(2, 'puegot')
print(motorcycles, "\n")

del motorcycles[4]                       # when you don't want to use the value later
print("after delete:",motorcycles, "\n")

stored = motorcycles.pop()               # when you want to use the value later
print(motorcycles)
print(stored, "\n")

first_moto = motorcycles.pop(0)
message = f"The first motorcycle i owned was a {first_moto.title()}"
print(message)
print(f"I currently gave these {motorcycles}", "\n")

motorcycles.remove('puegot')
print(motorcycles, "\n")              # when we don't know the index, we only know the value

motorcycles.append('yamaha')
motorcycles.append('hellcat')
print(motorcycles, "\n")

sell = 'dune'
motorcycles.remove(sell)
print(f"I want to sell {sell.title()}, cz it's old now.")
print(f"I'll only keep {motorcycles}")


guests = ['rohan', 'porosh', 'rifat', 'fujiwara']
print(f"\nOi {guests[0].title()}, bridge or eno ay", "\n")
print(f"oba {guests[-1].title()}, cholo cha khai", "\n")
print(f"{guests[2].title()} sasa adda oito ni ?", "\n")
print(f"{guests[1].title()}, let's go grab some pizza", "\n")

out = guests.pop(2)
print(f"oops {out} can't make it now.", "\n")

                                    #organizing a list

cars = ['bmw','lambo','audi','nissan','toyota']
print(cars,"\n")

cars.sort()                             #list changes permanently
print(cars)

cars.sort(reverse = True)               #list changes permanently
print(cars,"\n")
print(f"length of the car set is {len(cars)}.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("here is the main list:",cars)
print("here is the sorted one:",sorted(cars))           #doesn't change the list permanently
print("sorted in reverse:",sorted(cars, reverse=True))
print("main list again:",cars,"\n")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()       # reverse() twice to get the original order of the list
print(cars)
