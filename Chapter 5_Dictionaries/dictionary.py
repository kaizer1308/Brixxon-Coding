import os
os.system("cls")

student = {'name': 'sean', 'id': 7, 'course': 'BSC Cybersecurity'}

print('Student  details before deleting the value\n', student)

del student['course']  # Deleting the value of course

print('\n Student details after deleting the value\n', student)