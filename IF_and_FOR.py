alien_color = ['green', 'red', 'yellow']
if 'green' in alien_color:
    print('\nYou scored 5 points!')
if 'yellow' in alien_color:
    print('\nYou scored 10 points!\n')
if 'galaga' in alien_color:
    print('This should not print')

killed_alien = 'yellow'
if killed_alien == 'green':
    print('You scored 5 points!\n')
if killed_alien == 'yellow':
    print('You scored 10 points!\n')
if killed_alien == 'red':
    print('You scored 15 points!\n')

age = 25

if age < 2:
    print('That person is a baby')
if age < 4:
    print('That person is a toddler')
if age < 13:
    print('That person is a kid')
if age < 20:
    print('That person is a teenager')
if age < 65:
    print('That person is an adult\n')
if age > 65:
    print('That person is an elder')

usernames = ['ArchticStyx', 'MadiBear_0123', 'The_Professor_2112', 'Admin', 'Chonk']
for username in usernames:
    if username == 'Admin':
        print('Hello Admin, would you like to see a status report?')
    else:
        print(f'Welcome back {username}.')

usernames = []
if usernames:
    for username in usernames:
        if username == 'Admin':
            print('Hello Admin, would you like to see a status report?')
    else:
            print(f'Welcome back {username}.')
else:
    print('\nWe need to find some users!\n')

current_users = ['archy', 'madi', 'neil', 'vincent', 'chongus']
new_users = ['Archibald', 'Madi', 'Neilbert', 'Vincent', 'Chomngus']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry, that username is taken.')
    else:
        print('That username is available!')