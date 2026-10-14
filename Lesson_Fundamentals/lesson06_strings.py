# STRING MANIPULATION IN PYTHON
# built-in methods: len(), upper(), lower(), capitalize()

# String formatting, String concatination 

first_name = "Ada"
last_name = "Lovelace"
print(first_name, last_name, "!")
# Concactination
print("Hello" + " " + first_name + " " + last_name + "!")
#f-string
print(f"{first_name} {last_name}!")

greeting = "Hello"
first_name = "Ada"
print(greeting, first_name)


greeting = "Hello"
second_letter = greeting[1]
print(second_letter)

#String Slicing

word = "Super-cali-fragil-istic-expi-ali-docious"
print("\n The word is:", word)
print("The first letter is:", word[0])
print("The last letter is:", word[-1])
print("Range of letters (non-inclusive:)", word[3:7])
print("First five letters:", word[:5])
print("Everything after the first five letters:",word[5:])
print("Last seven letters:", word[-7:])
print("Step through every second character:", word[::2])
print("String in reverse:", word[::-1])

last_name = "LoveLace"
length = len(last_name)
print("Length of string:", length)

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.
# EXAMPLE OUTPUT:
# Enter your favorite quote: Those who believe in telekinetics, raise my hand.
# Your quote is 48 characters long.

quote = input("Enter your favorite quote: ")
length = (len(quote))
print(f"Your quote is {length} characters long.")

# Challenge 2:
# Ask the user to enter a word that is at least 7 characters long. 
# Print the 2nd through 6th characters.
# Use string slicing.

word = input("Enter a word that is at least 7 characters long: ")
print("The characters from 2 to 6 are", word[1:7])


# Challenge 3: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation or f-strings.
# Example output:
# Enter your first name: Ada
# Enter your last name: Lovelace
# Formatted name: Lovelace, Ada

first_name = input("Enter your First name: ")
last_name = input("Enter your Last name: ")
print(f"Formatted name: {last_name}, {first_name}")

