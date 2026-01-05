def factorial(number):
    fact = 1
    for i in range(number,1,-1):
        fact *= i
    return fact

number = int(input("Enter a number: "))
f = factorial(number)
print(f"The factorial of {number} is: ",f)