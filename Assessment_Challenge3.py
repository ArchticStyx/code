# Trevor White 3/27/22

# I'll begin addressing the user about what is going to happen and how to properly use the "Student Database Entry"
print('~~~ STUDENT DATABASE ENTRY ~~~\n')
print('Please input names, student ID number, and a list of grades for that student.')
numGrades = input("Enter the total number of grades you would like to submit for each student: ")
numGrades = int(numGrades) # using int() because we expect a number in return
print('\nBegin listing student information below.\n')
# I'll create a few dictionaries to be filled with user information as the code is executed:
studentInformation = {}
collectingData = True # I'll set a flag to initiate data collection for as long as the user wants
while collectingData:
    studentName = input('Student name: ')
    studentInformation[studentName] = studentName
    studentID = int(input('Student ID: '))
    studentInformation[studentID] = studentID
    studentGrades = 0
    for studentGrades in range(1, numGrades + 1):
        grade = int(input(f'Enter grade #{studentGrades}: '))
        studentGrades += 1
        studentInformation[grade] = grade

    repeat = input('Would you like to collect more student information(y/n)? ')
    if repeat == 'n':
        collectingData = False
print(studentInformation)


# https://tutorial.eyehunts.com/python/how-to-take-multiple-inputs-in-the-dictionary-in-python-example-code/

# pets = {
#     'vincent': ['cat', 'trevor'],
#     'brisket': ['cat', 'john'],
#     'madison': ['cat', 'megan'],
#     'rumor': ['dog', 'brynne'],
# }
# for name, info in pets.items():
#     print(f"\n{name.title()}'s animal type and owner are:")
#     for pinfo in info:
#         print(f"{pinfo.title()}")

# while decided_numOF_grades >= numberOF_grades:
#         for numberOF_grade in range(1, numberOF_grades):
#             input(f'Enter grade #{numberOF_grade}: ')
#         decided_numOF_grades += 1