# Even or Odd Checker – Ask the user for a number and determine if it's even or odd.




number = input("enter a number and I will tell you if it's even or odd: ")

while not number.isdigit():
    number = input("invalid. enter a valid number: ")

number = int(number)

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
