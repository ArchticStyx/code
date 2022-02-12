#Lists and Loops Assignment - Trevor White

#Start of Chapter 3

friends = ['Megan', 'John', 'Vincent']
print(friends[0])
print(friends[1].lower())
print(friends[2].upper())

guests = ['Getty Lee', 'Alex Lifeson', 'Neil Peart']
print(f'Hello, {guests[0]}, I would love to formally invite you to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[1]}, I would love to formally invite you to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[2]}, I would love to formally invite you to have dinner at Del Frisco with me and my friends.')

guests.remove('Neil Peart') #RIP The Professor
print('I regret to inform all guests that Neil Peart could not attend the dinner.')
guests.insert(2, 'Layne Staley')

print(f'Hello, {guests[0]}, You are still formally invited to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[1]}, You are still formally invited to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[2]}, I would love to formally invite you to have dinner at Del Frisco with me and my friends.')

print('I would like to inform you guys I have found a bigger table, more friends will be attending!')

guests.insert(0, 'Kendrick Lamar')
guests.insert(2, 'Cooper')
guests.append('Nate')

print(f'Hello, {guests[0]}, I would love to formally invite you to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[1]}, You are still formally invited to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[2]}, I would love to formally invite you to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[3]}, You are still formally invited to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[4]}, You are still formally invited to have dinner at Del Frisco with me and my friends.')
print(f'Hello, {guests[5]}, I would love to formally invite you to have dinner at Del Frisco with me and my friends.')

print('I regret to inform all guests, the table which was reserved for 7 of us will not be ready for the time we wanted.')
#I'm beginning to look like a really unreliable friend...
print(guests)
guests.pop(0)
print('I regret to inform you Kendrick, you have been dropped from the dinner arrangement.')
guests.pop(1)
print('I regret to inform you Cooper, you have been dropped from the dinner arrangement.')
guests.pop(2)
print('I regret to inform you Layne, you have been dropped from the dinner arrangement.')
guests.pop(2)
print('I regret to inform you Nate, you have been dropped from the dinner arrangement.')
print('Getty Lee and Alex Lifeson, you are both still invited to join me for dinner at Del Frisco.')
del guests[0]
del guests[0]
print(guests)

places = ['canada', 'germany', 'chile', 'new zealand', 'russia']
print(places)
print(sorted(places))
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#End of Chapter 3
#Start of Chapter 4

pizzas = ['pepperoni', 'banana pepper', 'bell pepper', 'old world pepperoni', 'bacon' ]
for pizza in pizzas:
    print(f'I love {pizza} pizza')
print('\nI thoroughly enjoy pizza\n')

animals = ['house cat', 'ocelot', 'tiger']
for animal in animals:
    print(f'A {animal} would make a great pet...')
print('\nIF you have enough money for food.')

numbers = list(range(1, 21))
print(numbers)

threes = list(range(3, 31, 3))
print(threes)

friends_pizzas = ['pepperoni', 'banana pepper', 'bell pepper', 'old world pepperoni', 'beef']