# Simple Calculator – Take two numbers and an operator (+, -, *, /) as input and perform the calculation.



first_number = input("enter first number: ")
while not first_number.isdigit():
    first_number = input("enter a valid first number: ")
first_number = int(first_number)

second_number = input("enter second number: ")
while not second_number.isdigit():
    second_number = input("enter a valid second number: ")
second_number = int(second_number)

operator = input("enter an operator (+, -, *, /):")
while not operator in ["+","-","*","/"]:
    operator = input("invalid operator. enter one of (+, -, *, /): ")
    
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number == 0:
        print("can't divide by zero")
    result = first_number / second_number
    
print(f"{first_number} {operator} {second_number} = {result}")