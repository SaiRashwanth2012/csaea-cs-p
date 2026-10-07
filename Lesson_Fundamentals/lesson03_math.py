

add = 7 + 2
print("Sum:", add)

subtract = 43 - 4
print("Difference:", subtract)

multiply = 7 * 2
print("Product:", multiply)

float_divide = 10 / 3
print("Float division:", float_divide)

integer_divide = 7 // 2
print("Integer division:", integer_divide)

mod = 7 % 2
print("Modulus:", mod)

exponent = 7 ** 2
print("Exponent:", exponent)

# PEMDAS

result = (2 + 3) * 4
print("Result 1:", result)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result 3:", result3)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5.  
# Create separate variables for width, height, and result. Print result. 

height = 5
width = 8
area = height * width
print("Area:", area)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. 
# (Use 3.14 for π.)  

radius = 7
pie = 3.14
circle_area = pie * (radius**2)
print("Circle Area:", circle_area)


# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks. 

book = 12.99
notebook = 3.50
total_cost_book = book * 3 
total_cost_notebook = notebook * 4
total_cost = total_cost_book + total_cost_notebook
print("Book:", total_cost_book, "\nNotebook:", total_cost_notebook, "\nTotal:", total_cost)

# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd. 

num = 57
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
