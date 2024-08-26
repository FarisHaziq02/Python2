#Creating dictionaries
student_grades = {"Alice": 85, "Bob": 90, "Charlie": 78, "Diana": 92}
print(student_grades["Bob"])

#Dictionaries operations
student_grades.update({"Eve": 88})
student_grades.update({"Alice": 95})
student_grades.pop("Charlie")
print(student_grades)

#Looping through dictionaries
for student, grade in student_grades.items():
    print(f"Student: {student}, Grade: {grade}")