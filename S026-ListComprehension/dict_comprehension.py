import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Create a dictionary with random scores
# student_scores = {
#     "Alex": 59,
#     "Beth": 95,
#     "Caroline": 76,
#     "Dave": 83,
#     "Eleanor": 75,
#     "Freddie": 53
# }

# Dict to loop through a list
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

# Create a dict which looks through scores and sees who got score over 60 and add them to a new dict
# passed_students = {
#     "Beth": 95,
#     "Caroline": 76,
#     "Dave": 83,
#     "Eleanor": 75,
# }

# Dict to loop through dict
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)
