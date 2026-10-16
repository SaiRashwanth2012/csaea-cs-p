# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math

sq_root = math.sqrt(25)
print("Square root:", sq_root)

round_up = math.ceil(4.5)
print("Round up:", round_up)

round_down = math.floor(4.8)
print(f"Round Down: {round_down}")

exponent = math.pow(2,5)
print(exponent)

# CONSTANT are variables that NEVER change. They are written in ALL CAPS

pi = math.pi
print(pi)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2
radius = 14 / 2
circle_area = math.pi * math.pow(radius, 2)
print(f"Circle area: {circle_area}")

# PYTHON RANDOM LIBRARY

# Python's library is a Pseudorandom Number Generator 

seed = 756
step1 = seed / 6.7
print("Step 1 is:", step1)
step2 = step1 - 800
print("Step 2 is:", step2)
step3 = step2 % 10
print("Step 3 is:", step3)
result = math.ceil(step3)
print("Your random num is:", result)

# Simple Random Number Generator
for n in range(5):
    calcs = seed + 2234 * 22 / 3
    randint = math.ceil(calcs)
    print(f"Simple random num gen: {randint % 10}")
    seed += 1

# Python random library

import random

random_integer = random.randint(1,100)
print(random_integer)

random_float = random.random()
print(random_float)

my_list = ["taco", "burrito", "enchilada", "quesadilla"]
random_selection = random.choice(my_list)
print(random_selection)

random.shuffle(my_list)
print(my_list)


# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it.

die = ["1", "2", "3", "4", "5", "6"]
die_roll = random.choice(die)
print(die_roll)

# Challenge 3: Random Square Root
# Use random library to pick a number between 1 and 75. Store it in "num".
# Use math library to find its square root.
# Print the number, its square root, and the square root rounded UP with math.ceil().

import random
import math

num = random.randint(1,75)
print("The number is:", num)
square_root = math.sqrt(num)
print(f"Square root of {num} is: {square_root}")
rounded_up = math.ceil(square_root)
print(f"Square root rounded up: {rounded_up}")

# Challenge 4: Power Roll
# Roll two dice with the random library: one is the "base," one is the "exponent."
# Use math library to raise the base to the exponent. (ie, based to the POWer of exponent)
# Print both rolls and the result as an integer (hint: int() removes the .0).

base = random.randint(1,6)
print("Base is:", base)
exponent = random.randint(1,6)
print("Exponent is:", exponent)
num = math.pow(base,exponent)
integer = int(num)
print("The final number is", integer)