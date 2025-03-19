# Sum of Digits - Ask the user for a number and calculate the sum of its digits.


number = input("enter a number: ")
result = 0
while not number.isdigit():
    number = input("enter a number: ")


for digit in number:
    digit = int(digit)
    result += digit
print(f"Sum of digits: {result}")