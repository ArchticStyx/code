 # Trevor White 4/3/22

def favoriteBook(title):
    """Naming my favorite book"""
    print(f"My favorite book is {title.title()}.")
favoriteBook('Python Crash Course, 2nd Edition')

def describeCity(cityName, cityLocation='Germany'):
    """listing city names and country origin"""
    print(f"\n{cityName.title()} is located in {cityLocation.title()}.")
describeCity(cityName='munich')
describeCity(cityName='ettal')
describeCity('Salzburg', 'Austria')

def makeAlbum(artistName, albumName, totalSongs=None):
    """return a dictionary with information about an album"""
    fullAlbum = {'Artist': artistName, 'Album': albumName}
    if totalSongs:
        fullAlbum['Songs'] = totalSongs
    return fullAlbum
urListeningTo = makeAlbum('Rush', 'The Chronicles')
print(f'\n{urListeningTo}')
urListeningTo = makeAlbum('Kendrick Lamar', 'DAMN.', totalSongs=14)
print(urListeningTo)

def Messages(unsentMessages, sentMessages):
    """We will send a few messages"""
    while unsentMessages:
        sendingMessage = unsentMessages.pop()
        print(f"\nSending message...")
        sentMessages.append(sendingMessage)
def showMessages(sentMessages):
    """We will show what messages have been sent"""
    print("\nThe following messages have been sent:")
    for sentMessage in sentMessages:
        print(f"\t{sentMessage}")
unsentMessages = ['I like grapes', 'There is a bobble head on my desk', 'It is 5:00 pm']
sentMessages = []
Messages(unsentMessages[:], sentMessages)
showMessages(sentMessages)

def sandwichMaker(*toppings):
    """making sandwiches specified by customer"""
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
sandwichMaker('turkey', 'pepperjack', 'banana pepper', 'jalepeno')

