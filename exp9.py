def factorial(n):
    if n<0:
        return None
    elif n==0 or n == 1 :
        return 1
    else:
        result = 1 
        for i in range(2,n+1):
            result*=i
        return result
    
num=int(input("Enter a positive integer: "))
fact=factorial(num)
if fact is None:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of{num} is : {fact}")    