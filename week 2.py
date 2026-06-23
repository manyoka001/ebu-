

def new_func():
    x = 7
    if x > 5:
        print("x is greater than 5")  # Output: x is greater than 5

    y = 5
    if y % 2 == 0:
        print("y is even")
    else:
        print("y is odd")  # Output: y is odd

    z = 7
    if z > 10:
        print("z is greater than 10")
        if z % 2 == 0:
            print("z is even")
        else:
            print("z is odd")
    else:
        print("z is 10 or less")

    score = 85
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'  # This block executes
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print(f"Your grade is {grade}")   # Output: Your grade is B

    # Loops
    # For loop - Iteration for a number of specified times
    print("For loop with specified iterations:")
    for i in range(1, 6):  # [1,2,3,4,5]
        print(f"Iteration {i}")  # Iterates from 1 to 5

    print("Using range to generate numbers:")
    # range(2,7) -> 2,3,4,5,6; adding 1 produces 3,4,5,6,7
    for num in range(2, 7):
        print(num + 1)  # Outputs numbers from 3 to 7

    print("Counting starting from 0:")
    for count in range(3):  # [0,1,2]
        print(count)  # Outputs 0, 1, 2

    fruits = ['pineapples', 'passion fruit', 'avocados' ]
print("While loop example:")
n = 0
while n < 5:
    n += 1
    print(f"n is {n}")  # Outputs n values from 1 to 5
print("Using break in a loop:")
    # While loop - Executes as long as a condition is True
print("While loop example:")
n = 0
while n < 5:
        n += 1
        print(f"n is {n}")  # Outputs n values from 1 to 5

print("Using break in a loop:")
for number in range(5):  # [0,1,2,3,4]
        if number == 3:
            print("Breaking the loop")
            break  # Exits the loop when number is 3
        print(number)

print("Using continue in a loop:")
for number in range(5):  # [0,1,2,3,4]
        if number == 3:
            print("Skipping this iteration")
            continue  # Skips the rest of the loop body when number is 3
        print(number)
print("Using continue in a loop (skip 2):")
for number in range(5):  # [0,1,2,3,4]
        if number == 2:
            print("Skipping number 2")
            continue  # Skips the rest of the loop when number is 2
        print(number)

    # Asking for a number and checking if it's even or odd
number = int(input("Enter a number: "))  # User inputs a number
if number % 2 == 0:
        print(f"{number} is even")
else:
        print(f"{number} is odd")

    # Asking for a score and assigning a grade
score = int(input("Enter your score: "))  # User inputs a score
score = int(input("Enter your score (0-100): "))

if score > 100 or score < 0:
    print("wrong score!!")
else:
    if score >= 90:
        print("You got an A!")
    elif score >= 80:
        print("You got a B!")
    elif score >= 70:
        print("You got a C.")
    elif score >= 60:
        print("You got a D.")
    else:
        print("You got an F.")

   # Continue the loop if the user enters an empty string

for i in range(5): 
    for j in range(10):
        name = input("Enter a name (leave empty to skip): ")
        if name == '':
            print("Skipped!")
            continue  # Skips the rest of the loop and starts the next iteration
        print(f"Hello, {name}!, number: {i}")
        
