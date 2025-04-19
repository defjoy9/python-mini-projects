# Task 1: Variable Practice
# Create a program that stores the following info in variables:

#     Your name
#     Your age
#     Your favorite color
#     Your hobby

# name = "Joy"
# age = "22"
# fav_color = "green"
# hobby = "painting"

# print(f"Hi, I'm {name} years old, i love the color {fav_color} and enjoy {hobby}")
# ------------------------------------------------------------------------------------

#  Task 2: Simple Age Calculator
# 🔹 Goal: Ask the user for their birth year, and calculate how old they are.

# Instructions:
#     Use input() to get the user's birth year.
#     Convert that input to an integer using int().
#     Subtract the birth year from the current year (you can just hardcode it like 2025 for now).
#     Print a message like:
#     "You are 22 years old."

#birth_year = int(input("enter your birth year: "))
#current_year = 2025
#age = current_year - birth_year
#print(f"You are {age} years old")
# ------------------------------------------------------------------------------------

# 🧮 Simple BMI Calculator
# Goal: Use user input and arithmetic to calculate Body Mass Index (BMI).
# ✨ Instructions:
# Ask the user for:
#     Their weight in kilograms (kg)
#     Their height in meters (m)

# weight = float(input("enter your weight (in kilograms): "))
# height = float(input("enter your height (in meters): "))

# bmi = weight / (height ** 2)

#print(f"your BMI is {bmi}")
# ------------------------------------------------------------------------------------
# ⭐ Temperature Conversion Program

# Task:
# Create a program that:

#     Asks the user to input a temperature value.

#     Asks them if the temperature is in Celsius or Fahrenheit.

#     Converts the temperature to the other unit.

#     Prints the result.

# value = int(input("enter the temperature: "))
# temp = input("Is this in (C)elsius or (F)ahrenheit?: ").lower()

# if temp == 'c':
#     fahrenheit = (value * 9 / 5) + 32
#     print(f"Result: {value}°C is {fahrenheit:.2f}°F")
# elif temp == 'f':
#     celsius = (value - 32) * 5 / 9
#     print(f"Result: {value}°F is {celsius:.2f}°C")
# else:
#     print("Invalid input. Please enter 'C' or 'F'.")

# ------------------------------------------------------------------------------------

# ⭐ Task: Movie Ticket Checker 🎟️
# Ask the user for:

#     Their age
#     Whether they have a student ID (yes or no)
# Then check if they qualify for a discounted movie ticket:
#     If they are under 18, or
#     They have a student ID
# Print a message like:
#     ✅ "You qualify for a discounted ticket!"
#     ❌ "Sorry, no discount available."

age = int(input("Enter your age: "))
student_id = input("Do you have a student ID? (yes/no): ").lower()

if age < 18 or student_id == "yes":
    print("You qualify for a discounted ticket!")
else:
    print("Sorry, no discount available.")