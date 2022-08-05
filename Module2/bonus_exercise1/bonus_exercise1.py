exam_points = {
    "Mariusz": 30,
    "Mateusz": 55,
    "Marta": 76,
    "Roman": 30,
    "Arleta": 59,
    "Adrian": 96,
    "Monika": 91,
    "Andrzej": 22,
    "Krzysztof": 83,
    "Krystyna": 93,
    "Piotr": 44,
    "Dawid": 10,
    "Agnieszka": 15,
}

failed_students = []
top_students = []
best_student = ("", 0)

for student, grade in exam_points.items():
    if grade < 61:
        failed_students.append(student)
    if grade > 91:
        top_students.append(student)

best_students = [
    name for name, grade in exam_points.items() if grade == max(exam_points.values())
]
best_student_name = best_students[0]

# Alternative:
# best_student_name = max(exam_points, key=exam_points.get)

best_student = (best_student_name, exam_points[best_student_name])

print("Failed students:")
print(failed_students)

print("Top students:")
print(top_students)

print("Best student:")
print(best_student)
