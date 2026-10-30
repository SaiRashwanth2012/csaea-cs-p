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
    result = []

    for _ in range(times):
        num *= 2
        result.append(num)

    return result


print(doubler(1, 5))
print("result: -->", result)





