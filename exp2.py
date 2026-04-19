print("choose a shape")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = input("Enter your choice(1,2 or 3):")

if choice == "1":
    r=float(input("Enter radius: "))
    area = 3.14 * r * r
    print("Area of circle =" , area)

elif choice == "2":
  l = float(input("Enter length: "))
  b = float(input("Enter breadth: "))
  area = l* b
  print("Area of rectangle =", area)

elif choice == "3":
   h = float(input("Enter height: "))
   b = float(input("Enter base: "))
   area = 0.5 * h* b
   print("Area of triangle =", area)

else:
   print("Invalid choice")