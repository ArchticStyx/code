#Trevor White 02/28/2022 Assessment Challenge 2
numbers = range(42, 501)
for num in numbers:
    if num % 3 == 0 and num % 5 == 0: #I ended up with this statement at the end of the program, moving it to the beginning required this to be checked first.
        print(f'{num} is divisible by both 3 & 5')
    #I originally was using all 'if' statements, which coupled with my corrected issue above, would print all statements if they were divisible by 3, 5, and both, created unnecessary response length
    elif num % 3 == 0:
        print(f'{num} is divisible by 3')
    elif num % 5 == 0:
        print(f'{num} is divisible by 5')
    #if num % 3 != 0 and num % 5 != 0: 
    # Saved a line of work by using 'else' statement:
    else:
        print(num)