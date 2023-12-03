# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum_heights = 0
num_heights = 0

for student_height in student_heights:
    sum_heights += student_height
    num_heights += 1

avg_heights = round(sum_heights / num_heights)
print(f"The average heights are {avg_heights}")

# No for loop
total_height = sum(student_heights)
number_of_students = len(student_heights)
