
# Question 4
print("Start of # Question 4")
score = 56
if score >= 90 and score <= 100 :
    print("A")
elif score >= 80 and score <= 90:
    print("B")
elif score >= 70 and score <= 80:
    print("C")
elif score >= 60 and score <= 70:
    print("D")
elif score >= 50 and score <= 60:
    print("F")

print("End of # Question 4")

# 5 Login Screen
print("Start of # Question 5")

password = "csaea2026"
attempt = "csaea2026"
if attempt == "csaea2026":
    print("Password accepted")
else:
    print("Access Denied")
print("End of # Question 5")


# Question 8
print("Start of # Question 8")
first = "Ada"
last = "Lovelace"
school = "CSAEA" 
print(f"Hello, my name is {first} {last} from {school}.")
print("End of # Question 8")

# Question 11
print("Start of # Question 11")
start = 10
while start > 0:        
    print(start)
    start -= 1
if start == 0:
    print ("Liftoff")
print("End of # Question 11")

# Question 15
print("Start of # Question 15")
grades = [88, 65, 72, 91, 54, 70]
passing = 70

if grades[0] >= 70:
    print("0 passed")
else:
    print("0 Failed")
if grades[1] >= 70:
    print("1 passed")
else:
    print("1 Failed")
if grades[2] >= 70:
    print("2 passed")
else:
    print("2 Failed")
if grades[3] >= 70:
    print("3 passed")
else:
    print("3 Failed")
if grades[4] >= 70:
    print("4 passed")
else:
    print("4 Failed")
if grades[5] >= 70:
    print("5 passed")
else:
    print("5 Failed")
print("End of # Question 15")
# Question 3
print("Start of # Question 3")
import math

fahrenheit = 32

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is {(celsius, 2)}°C")
print("End of # Question 3")

# Question 20
print("Start of # Question 20")
speed_limit = 55
speed = 100

mph_over = speed - speed_limit

if mph_over <= 0:
    result = "No violation"
elif mph_over <= 10:
    result = "Warning"
elif mph_over <= 20:
    result = "$100 fine"
else:
    result = "$250 fine"

print(result)
print("End of # Question 20")
# Question 7
print("Start of # Question 7")
height = 50
age = 8
has_adult = True
if height >= 48:
   if age >= 10 or has_adult == True:
        print("You may ride.")
else:
        print("You may NOT ride.")

print("End of # Question 7")

# Question 18
print("Start of # Question 18")
import random
playlist = ["Intro", "Song A", "Song B", "Finale"]
random.shuffle(playlist)
print(playlist)

print("End of # Question 18")

# Question 17
print("Start of # Question 17")
import math
 
minutes_parked = 50
block_length = 15
cost_per_block = 1

amount_owed=math.ceil((minutes_parked/block_length)*cost_per_block)

print("You owe $",amount_owed)

print("End of # Question 17") 
