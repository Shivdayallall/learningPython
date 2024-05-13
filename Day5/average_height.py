# print out the average height of the student from the array and the amount of student and the sum of the height
student_height = [178, 156, 165, 171, 187]
sum_height = 0
avg_height = 0
number_students = 0

for students in student_height:
    number_students += 1
    sum_height += students
    avg_height = sum_height / number_students
print(f"number of students: {number_students}")
print(f"total height: {sum_height}")
print(f"avergae height is: {avg_height}")