import re


cars = ['nissan', 'aston martin', 'mclaren', 'bugatti', 'toyota']
for car in cars:
    if car == 'mclaren':
        print(car.upper())
    else:
        print(car.title())

# requested_car = 'Nissan'
# if requested_car != ['aston martin', 'mclaren', 'bugatti', 'toyota']:
#     print("This isn't a fucking Nissan")

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)
# print('pepperoni' in requested_toppings)


# banned_users = ['jennifer', 'torin', 'your mom']
# user = 'megan'
# if user not in banned_users:
#     print(f'{user.title()}, you can sugondeez if you wish.')

# car = 'nissan'
# print("Is car == 'nissan'? I predict True.")
# print( car == 'nissan')

age = 17
if age >= 18:
    print('You are old enough to vote!')
else:
    print('You are not old enough to vote.')
    print('Fuck off')

age = 21
if age < 4:
    print('Your admission price is $0')
elif age < 18:
    print('Your admission price is $20')
else:
    print('Your admission price is $30')

#alternatively:

age = 21
if age < 4:
    price = 0
elif age < 18:
    price = 20
else:
    price = 30

print(f"Your admission price is ${price}.\n")

# requested_toppings = ['pepperoni', 'old world pepperoni', 'banana pepper', 'bell pepper']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'banana pepper' in requested_toppings:
#     print("Adding banana pepper.")
# if 'old world pepperoni' in requested_toppings:
#     print('Adding old world pepperoni.')

print('\nFinished making your pizza\n')

toppings = ['pepperoni', 'old world pepperoni', 'banana pepper', 'bell pepper', 'mushrooms', 'ground beef']
for topping in toppings:
    if topping == 'banana pepper':
        print('Sorry, we are out of Banana peppers.')
    else:
        print(f'Adding {topping}.')
print('\nFinished making your new pizza.\n')

requested_toppings = ['bacon', 'provalone', 'crickets', 'pepperoni']
for requested_topping in requested_toppings:
    if requested_topping in toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f'Sorry we do not have {requested_topping}.')
print('\nFinished making your pizza.')