print("Student Enrollment Set Operations")

cet_students = {"Alice", "Bob", "Charlie", "Frank"}
jee_students= {"Charlie", "David", "Frank", "Eve"}
neet_students= {"Alice", "Frank", "George", "Hannah"}

print(f"CET Students: {cet_students}")
print(f"JEE Students: {jee_students}")
print(f"NEET Students: {neet_students}")

#Union of all students

all_students = cet_students.union(jee_students).union(neet_students)
print(f"All Students (Union): {all_students}")

#Intersection of students appearing for all exams
all_exams_students = cet_students.intersection(jee_students).intersection(neet_students)
print(f"Students appearing for all exams (Intersection): {all_exams_students}")

#Students appearing for CET but not for JEE
cet_not_jee = cet_students.difference(jee_students)
print(f"Students appearing for CET but not for JEE (Difference): {cet_not_jee}")

#Students appearing for JEE but not for NEET
jee_not_neet = jee_students.difference(neet_students)
print(f"Students appearing for JEE but not for NEET (Difference): {jee_not_neet}")

#Students appearing for NEET but not for CET
neet_not_cet = neet_students.difference(cet_students)
print(f"Students appearing for NEET but not for CET (Difference): {neet_not_cet}")