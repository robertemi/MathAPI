students = []
with open('students.txt', 'r') as f:
    students = [line.strip() for line in f]

with open('filtered.txt', 'w') as f:
    f.writelines(student + '\n' for student in students if student[0] in 'AEIOUaeiou')
