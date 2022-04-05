# Trevor White 4/3/22

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}.")
greet_user('Pickle')

def describe_car(car_type, car_name='GT-R'): # ='GT=R' used if you notice a repeating pattern
    """Display info about cars"""
    print(f"\nI have a {car_type}.")
    print(f"My {car_type}'s model is a {car_name}.\n")
describe_car('Nissan', 'Skyline GT-R')
describe_car(car_type='Toyota', car_name='Corolla')
describe_car(car_type='Nissan') # this will auto fill as you described it above
#describe_car() this wouldn't work, not enough arguments provided

# this example will provide an optional parameter for middle name if provided
def get_formatted_name(first, last, middle=''):
    """return a full name, neatly formatted."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
musician = get_formatted_name('neil', "'The Professor'", 'peart')
print(musician)
musician = get_formatted_name('getty', 'lee')
print(f"musician\n")

def build_animal(animal_type, animal_model, age=None):
    """return a dictionary of info about an animal"""
    animal = {'type': animal_type, 'model': animal_model}
    if age:
        animal['age'] = age
    return animal
theAnimal = build_animal('cat', 'american shorthair tabby', age=1)
print(theAnimal)

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
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

def greetings(names):
    """Print a greeting to each person in the list"""
    for name in names:
        msg = f"\nHello, {name.title()}."
        print(msg)
people = ['Vincent', 'John', 'Mayberry']
greetings(people)

unprintedDesigns = ['phone case', 'robot thing', 'dodecahedron']
completedModels = []
while unprintedDesigns:
    currentDesign = unprintedDesigns.pop()
    print(f"Printing model: {currentDesign}")
    completedModels.append(currentDesign)
print("\nThe following models have been printed:")
for completedModel in completedModels:
    print(completedModel)

# alternitavely:

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left
    Move each design to completed models after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"\nPrinting model: {current_design}")
        completed_models.append(current_design)
def showCompletedModels(completed_models):
    """Show all of the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'thingy']
completed_models = []
print_models(unprinted_designs[:], completed_models)
showCompletedModels(completed_models)

def makePizza(size, *toppings):
    """pizza shit."""
    print(f"\nMaking a {size}-inch pizza witht the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
makePizza(16, 'pepperoni')
makePizza(18, 'banana pepper', 'extra cheese')

def makeProfile(first, last, **userInfo):
    """build a dictionary containing everything we know about user"""
    userInfo['firstName'] = first
    userInfo['lastName'] = last
    return userInfo
userProfile = makeProfile('vincent', 'white',
location='Celina',
field='cat')
print(f'\n{userProfile}')