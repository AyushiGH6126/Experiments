print("Division calculator with exception handling")

try:
    num1=float(input("Enter the numerator:"))
    num2=float(input("Enter the denominator:"))

    result=num1/num2

    print(f"The result of {num1}divided by {num2} is {result}")

except ZeroDivisionError:
    print("Error division by zero is not allowed")

except ValueError:
    print("Error: Invalid input, please enter numerical values")

except Exception as e:
    print(f"An unexpected error occurred : {e}")

input("Press enter to exit...")
