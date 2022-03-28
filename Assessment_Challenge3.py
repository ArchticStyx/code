# Trevor White 3/27/22

# I'll begin addressing the user about what is going to happen and how to properly use the "Student Database Entry"
print('STUDENT DATABASE ENTRY')
print('Please input names, student ID number, and a list of grades for that student.')
numberOF_grades = input("Enter the total number of grades you would like to submit for each student: ")
numberOF_grades = int(numberOF_grades) # using int() because we expect a number in return
print('\nBegin listing student information below.')
data_collection = True # I'll set a flag to initiate data collection for as long as the user wants
decided_numOF_grades = 1
entered_grades = {}
while data_collection:
    decided_numOF_grades <= numberOF_grades:
        for numberOF_grade in range(1, numberOF_grades):
            input(f'Enter grade #{numberOF_grade}: ')
    decided_numOF_grades += 1
