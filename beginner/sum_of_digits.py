# Sum of Digits - Ask the user for a number and calculate the sum of its digits.


number = input("enter a number: ")
result = 0
while not number.isdigit():
    number = input("enter a number: ")


result = sum(int(digit) for digit in number)

print(f"sum of digits: {result}")