import re

phone = input("Enter phone number: ")
email = input("Enter email: ")

phone_pattern = re.compile(r'^\d{10}$')
email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@eng\.rizvi\.edu\.in$')
if re.match(phone_pattern, phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")