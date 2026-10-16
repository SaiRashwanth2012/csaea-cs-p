# User Input in Python
import math
import random
name = input("Enter your name: ")
print(f"Hello {name}")

print(type(name))

age = input("Enter your age: ")
print(f"Your age is {age}")

print(type(age))

age_converted = int(age)
print(type(age_converted))

height = float(input("Enter your height: "))
print(f"You are {height} feet tall")
print(height + 1)

#Challenge 1: Favorite Color
#Ask the user for their favorite color and print out a message using it.

color = input("Enter your favorite color: ")
print(f"Your favorite color is {color}")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
final_num = number1 + number2
print(f"The sum is: {final_num}")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# pi radius squared 

diameter = float(input("Enter the diameter: "))
radius = diameter / 2
area = 3.14159 * radius * radius
print("The area is:", area)

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.
sides = int(input("Enter the number of sides on the die: "))
roll = random.randint(1, sides)
print(f"You rolled a {roll}")