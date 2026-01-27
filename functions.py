# Simple Function
def greet():
    return "Hello World"

#Function with Parameters
def Hello(name):
    print("Hello " + name)
Hello("dip")

# Function with Return Value
def add(x, y):
    return x + y
print(add(2, 3))

# Even Odd Function
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(2))
print(check_even_odd(9))

# Default Parameter Values
def sayHello(name="User"):
    print("Hello", name)
sayHello()
sayHello("Shubh")

# Multiple Return Values
def calculate(a, b):
    return a+b, a-b, a*b
sum, diff, mul = calculate(10, 5)
print(sum, diff, mul)

# Recursive Function factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

# Function with User Input
def square(num):
    return num * num
n = int(input("Enter a number: "))
print(square(n))

# function using lists
def find_max(numbers):
    return max(numbers)

print(find_max([10, 25, 7, 40]))



