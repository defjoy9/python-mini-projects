import math


principal = float(input("enter your initial investment: "))
rate = float(input("enter annual rate interest (as %): "))
time = int(input("enter time (in years): "))
number = int(input("enter number of times interest is compounded per year: "))

rate = rate /100
total = principal * pow((1 + rate / number), number * time)
print(f"total:{total:.2f}")