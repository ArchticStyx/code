#My name is Trevor White, this is my assessment challenge

first = "trevor"
last = "white"

gradeA = 89
gradeB = 67
gradeC = 83
gradeD = 60
gradeE = 56
gradeF = 59
#He didn't do so great in school...

full_name = (first + last)
full_name_cap = (first.title() + " " + last.title())

print(f"Your quiz grades are, {gradeA}, {gradeB}, {gradeC}, {gradeD}, {gradeE}, {gradeF}.")
gpa = (gradeA + gradeB + gradeC + gradeD + gradeE + gradeF) / 6
print(f"{full_name_cap}'s grade point average is {gpa}")

#Had some trouble getting lines 18, 19 to work. Originally I tried putting the "grades" into an f string, couldn't get the
#whole string to work. Something like print(f"{full_name}'s grade point average is " (gradeA + gradeB) / 6) which it didn't like

new_gradeA = gradeA + 5
new_gpa = (new_gradeA + gradeB + gradeC + gradeD + gradeE + gradeF) / 6
print(f"{full_name_cap}'s new grade point average is {new_gpa}")
#Couldn't manage to get the C :(