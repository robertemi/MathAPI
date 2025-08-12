# list with squares

squares = [i * i for i in range(1, 11)]
print(squares)


# set with nums

nums = {i for i in range(1, 51) if i % 7 == 0}
print(nums)


# dict with passed students

score = {
    "Alice": 85, 
    "Bob": 59, 
    "Charlie": 92
    }

passed = {stud: score[stud] for stud in score.keys() if score[stud] > 60}
print(passed)


# weekly attendance log

students = ["Michael", "David", "Liza"]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

attendance = {
    student: {
        day: day in ["Mon", "Wed"]  # True for Mon/Wed, False otherwise
        for day in weekdays
    }
    for student in students
}

print(attendance)