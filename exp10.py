def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check divisibility from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

print("Prime number checker")
# Taking input from user
num = int(input("Enter a number: "))

# Function call
if is_prime(num):
    print(f"{num} is a Prime number")
else:
    print(f"{num} is NOT a Prime number")