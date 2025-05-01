# Goal: Help the user calculate how much interest they'll earn on their money over time.


principal = float(input("enter principal amount: "))
rate = float(input("enter annual rate (in %): "))
time = int(input("enter time (in years): "))

interest = (principal * rate * time) / 100

print(f"Interest amount: {interest}")
print(f"Total amount: {principal + interest}")