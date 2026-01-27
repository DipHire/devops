print("Hello, World!")

print("name","Dip",123,sep="-",end="***\n")

print("dip", end =" ")
print("hire")

# 1. Taking string input
name = input("Enter your name: ")
print(type(name))

# 2. Taking multiple inputs in one line
a, b = input("Enter two numbers separated by space: ").split()

# 3. Type conversion
a = int(a)
b = int(b)

# 4. Taking float input
radius = float(input("Enter radius of circle: "))

# 5. Expressions and calculations
sum_ab = a + b
product_ab = a * b
area = 3.14 * radius * radius

# 6. Formatted output using f-string
print(f"\nHello {name}")
print(f"Sum of {a} and {b} = {sum_ab}")
print(f"Product of {a} and {b} = {product_ab}")
print(f"Area of circle = {area}")

# 7. Using sep and end
print("\nValues:", a, b, radius, sep=" | ", end=" | END")

print()
# splitting a string
data = "10,20,30,40"
numbers = data.split(",")
print(numbers)
print(type(numbers))
print(len(numbers))

