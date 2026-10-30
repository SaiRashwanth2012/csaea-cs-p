# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, 
# and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp


def say_hi():
    print("Hi")

def say_bye():
    print("Bye")

say_hi() # calling the fuction 
say_bye()
say_hi()
say_hi()
say_bye()

# Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a function's PARAMETER

def express_this(e):
    return e

expression = express_this(1*5)

print(expression)

def greeter(name):
    return f"Hi {name}"
    
first = greeter("Jojo")
second = greeter("Bizbo")
third = greeter("Hoppy")
print(first, second, third)

def remainder(a,b):
    return a % b
    
result = remainder(10,9)    
print(result)

def is_far(distance):

    if distance >= 100:
        return "That's far"
    if distance < 100 and distance > 20:
        return "That's not too far"
    if distance < 20:
        return "Hey that's pretty close by!"
    
distance1 = is_far(900)
distance2 = is_far(50)
distance3 = is_far(14)
distance4 = is_far(230)
print(distance1, distance2, distance3, distance4)
 
# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number
# Write a function named doubler(num, times) that has TWO parameters: 
# First parameter:  the number i want doubled
# Second paramater: how many times the loop should run 
# Tools: loops, lists [], .append()

#Example output:
# doubler(1, 5)
# result --> [2, 4, 8, 16, 32]

def doubler(num, times):
    doubled_numbers = []

    for n in range(times):
        num *= 2
        doubled_numbers.append(num)
        print(doubled_numbers)
    
    print(doubled_numbers)
    return doubled_numbers

doubler(1,5)



# For Challenges 1 - 3, first write pseudocode, then solve in code.
 
# Challenge 1. 
# Make a calculator with 4 procedures that accept two arguments each. 
# 1) add any two numbers and print and return the result
# 2) subtract any two numbers and print the result
# 3) divide any two numbers and print the result
# 4) multiply any two numbers and print the result 

print("Add:")
def adder(a,b):
    
    return a + b
sum1 = adder(4,5)
print(sum1)

print("Subtract:")
def subtract(a,b):
   
    return a - b
sum2 = adder(6,5)
print(sum2)

print("Multiply:")
def multiply(a,b):
    
    return a * b
sum3 = multiply(5,7)
print(sum3)

print("Divide:")
def divide(a,b):
    
    return a / b
sum4 = divide(12,3)
print(sum4)

# Challenge 2
# Make a function called average that:
# 1) accepts three numbers
# 2) returns the average
# 3) print the returned value outside the function

print("Average:")
def average(a, b, c):
    return (a + b + c) / 3

result = average(10, 20, 30)
print(result)

# Challenge 3
# Make a function called is_even that:
# 1) accepts one number
# 2) prints "Even" if the number is even
# 3) prints "Odd" if the number is odd

print("Even or Odd:")
def is_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
number = is_even(3)

# Challenge 4
# Use the pseudocode below to write code:
# Make a function called "analyze_word" that counts how many vowels and consonants are in a word
# Tools: uses a for loop, IF/THEN statement, "aeiou".

# The function analyze_word accepts one argument, a single word (string):
# Initialize two variables:
# vowelCount set to 0
# consonantCount set to 0
# Use a loop to iterate through each character in the word.
# Inside the loop, use an IF/ELSE statement:
# If the character is a vowel (a, e, i, o, u), increment vowelCount.
# Otherwise, increment consonantCount.
# After the loop ends: 
# 	return a f-string that states how many vowels and how many consonants are in the word.

# Call the function with a sample one-word string and print the returned result outside the function

print("Constant and Vowel Count")
def analyze_word(word):
    vowelCount = 0
    consonantCount = 0

    for character in word.lower():
        if character in "aeiou":
            vowelCount += 1
        else:
            consonantCount += 1

    return f"{word} has {vowelCount} vowels and {consonantCount} consonants."


result = analyze_word("pneumonoultramicroscopicsilicovolcanoconiosis")
print(result)



    
    







    