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

seed = 756.22
step1 = seed / 6.7
print("Step 1 is:", step1)
step2 = step1 - 800
print("Step 2 is:", step2)
step3 = step2 % 10
print("Step 3 is:", step3)
result = math.ceil(step3)
print("Your random num is:", result)





