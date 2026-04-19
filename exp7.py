print("--- Student Records Manager ---\n")

student_records = {
    "251P005": {"name": "Shibu", "grade": "A", "attendance": 45},
    "251P034": {"name": "Junaid", "grade": "A+", "attendance": 95},
    "251P006": {"name": "Dhanashree", "grade": "A-", "attendance": 100}
}

print(f"Current Students: {student_records}")

print("\nAdding New Student:-")
UIN = input("Enter Student UIN:")
name = input("Enter Student Name:")
grade = input("Enter Student Grade:")
attendance = input("Enter Student Attendance:")

student_records[UIN] = {
    "name": name,
    "grade": grade,
    "attendance": attendance
}

print(f"Updated Students: {student_records}")

print("\nUpdating Student:-")
UIN = input("Enter Student UIN:")
print(f"Student Detail: {student_records[UIN]}")
grade = input("Enter Student Updated Grade:")
attendance = input("Enter Student Updated Attendance:")

student_records[UIN] = {
    "name": student_records[UIN]["name"],
    "grade": grade,
    "attendance": attendance
}

print(f"Updated Students: {student_records}")

print("\nDeleteing Student:-")
UIN = input("Enter Student UIN to Delete:")
print(f"Student Detail: {student_records[UIN]}")

student_records.pop(UIN)

print(f"Updated Students: {student_records}")