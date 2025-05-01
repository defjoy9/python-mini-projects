#Challenge: Find the Most Frequent Character - Ask the user for a sentence and find the most frequently occurring character (excluding spaces).


# sentence = input("Type a sentence: ")
# ocurrrence = {}
# max_char = ""
# max_count = 0

# for letter in sentence:
#     if letter != " ":
#         if letter not in ocurrrence:
#             ocurrrence[letter] = 0  # Initialize if not present
#         ocurrrence[letter] += 1  # Increment the count

# for char, count in ocurrrence.items():
#     if count > max_count:
#         max_char = char
#         max_count = count

# print(f"{max_char}: {max_count}")

# Print numbers from 1 to 50, but for multiples of 3, print "Fizz" instead of the number, and for multiples of 5, print "Buzz". 
# If a number is a multiple of both 3 and 5, print "FizzBuzz".


for i in range(51):
    if not i % 3 and not i % 5:
        print("FizzBuzz")
    if not i % 3:
        print("Fizz")
    elif not i % 5:
        print("Buzz")

    else:
        print(i)

#Dictionaries & User Input 
# Create a dictionary storing 3 favorite foods with their prices. 
# Ask the user to enter a food name, and if it exists in the dictionary, print the price. Otherwise, print "Food not found".

foods = {
    "pizza": 35.00,
    "kebab": 26.50,
    "ice cream": 3.60
}

food = input("enter food name: ")

if food not in foods:
    print("Food not found")
else:
    print(f"{food}: {foods.get(food)}")


#Random Guessing Game (Modifications) 
# Modify your number guessing game so that it also counts the number of attempts before the user guesses correctly.

import random

lowest_guess = 0
highest_guess = 50

guess = random.randint(lowest_guess,highest_guess)
user = 0
guesses = 0 
is_running = True


while is_running:
    user = int(input("enter your guess: "))
    guesses += 1
    if guess > user:
        print("Too low!")
        
    elif guess < user:
        print("Too high!")
    else:
        print(f"correct! it's {guess}\n it took you {guesses} guesses")
        is_running = False

# Functions & Default Arguments
# Write a function greet(name, greeting="Hello") that prints a custom greeting message.
# If no greeting is provided, it should default to "Hello".

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"  # Return instead of print

print(greet("Duh", "Welcome to today's celebration"))