student_scores = {
    "billy": 81,
    "bob": 56,
    "lilly": 78,
    "mandy": 98
}

student_grades = {}
for student in student_scores:
    #print the value base on the current key
    score = student_scores[student]
    if score >= 91:
        student_grades[student] = "outstanding"
    elif score >= 81:
        student_grades[student] = "Excellent"
    elif score >= 71:
        student_grades[student] = "you did okay"
    else:
        student_grades[student] = "you failed"
print(student_grades)


