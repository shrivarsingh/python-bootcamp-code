student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# # Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(f"\nstudent_data_frame:\n{student_data_frame}")

# # Looping through a DataFrame
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Pandas has in built Loop
# Loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    print("__________________________________________")
    print(f"\nindex:\n{index}")
    print(f"\nrow:\n{row}")
    print(f"\nrow.student:\n{row.student}")
    print(f"\nrow.score:\n{row.score}")
    if row.student == "Angela":
        print("codition checked if Angela")
print("__________________________________________")
