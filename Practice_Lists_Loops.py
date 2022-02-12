#Practice for Lists & Loops Assignment - Trevor White
"LISTS"
bikes = ['green', 'red', 'blue']
print(bikes[0].upper())
print(bikes[-1].title())
message = f"My First Bicycle was {bikes[0].upper()}"
print(message)

#bikes[0] = 'purple'
bikes.append('pruple')
print(bikes)
bikes.insert(0, 'orange')
print(bikes)
del bikes [3]
print(bikes)

popped_bike = bikes.pop() #this can also be used to "pop" any item > pop(0) 
print(bikes)
print(popped_bike) 
print(f'The last bicycle I owned was not {popped_bike.title()}')

first_owned = bikes.pop(1)
print(f'The first bike I owned was {first_owned.title()}')
print(bikes)
bikes.remove('orange')
print(bikes)

bad_color = 'red'
bikes.remove(bad_color)
print(bikes)

cars = ['honda', 'toyota', 'chevy', 'ford', 'nissan', 'volkswagon']
#cars.sort() ... this is permanent
#print(cars)

#cars.sort(reverse=True) ... again also permanent
#print(cars)

# print('Original List:')
# print(cars)
# print('\nHere is the sorted list:')
# print(sorted(cars)) #this is temporary
# print('\nOriginal List:')
# print(cars)

print(cars)
cars.reverse() #simply reverses order of list
print(cars)

len(cars)

'_____________________________________________________________________________________'
"LOOPS"

places = ['germany', 'chile', 'new zealand', 'russia', 'canada']
for place in places:
    print(place)

places = ['germany', 'chile', 'new zealand', 'russia', 'canada']
for place in places: 
    print(f'{place.title()} is an amazing place.')
    print(f'I cant wait to go to {place.title()}.\n')

print('Some day I will get to travel to the places I want to')

for value in range(1, 6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

threes = list(range(3, 31, 3))
print(threes)