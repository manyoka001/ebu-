def greet():
	print("Hello, Welcome to the Python function tutorial!")


greet()  # Call to the function
def greet_person(name):
	print(f"Hello, {name}! Welcome to the Python function tutorial!")

greet_person("Anne")  # Call to the function with an argument
def add(a, b):
	return a + b  
result = add(10, 5)  # Call and store the result
print(f"The result is: {result}")
name = input("Anne: ") 
print(f"Hello, {name}")  # Using print
print(type(name))  # Using type
def multiply(x, y):
	    return x * y
print(multiply(4, 5))  # Calling the UDF


square = lambda x: x * x  # Lambda function
print(square(6))  # Output: 36
multiply_lambda = lambda x, y: x * y
print(multiply_lambda(3, 4))  # Output: 12
def multiply_and_add(x, y, z):
    result = multiply(x, y)  # Calls the multiply function
    return add(result, z)     # Adds z to the product

print(multiply_and_add(2, 3, 5)) 
name = "Africa"  # Global variable

def greet_local():
    name = "Kiambu"  # Local variable
    print(f"Inside function: {name}")
greet_local()  # Output: Inside function: Local Name
def my_function(*args):
    for arg in args:
        print(arg)

my_function(1, 2, 3, "Hello")  # Arbitrary number of arguments
def greet_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
greet_kwargs(name="Anne", age=29, city="Nairobi")
def greet_default(name="Stranger"):
    print(f"Hello, {name}!")
greet_default()  # Output: Hello, Stranger!
greet_default("Anne")  # Output: Hello, Anne!
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
def apply_function(func, value):
    return func(value)
def square(x):
    return x * x
print(apply_function(square, 4))  # Output: 16
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]
def greet():
    print("Hello from inside the loop!")
for i in range(5):
    greet()  # The loop iterates 5 times, but 'i' is not used inside the function
def square(number):
    return number ** 2
for i in range(1, 6):
    print(f"The square of {i} is: {square(i)}")
def to_uppercase(string):
    return string.upper()
names = ["Anne", "python", "functions", "loop"]
for name in names:
    print(f"{name} in uppercase is: {to_uppercase(name)}")