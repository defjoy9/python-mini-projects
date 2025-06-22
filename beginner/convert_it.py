# Create a program that:

#     Asks the user to enter the number of minutes they’ve exercised today.
#     Converts that number into hours (with decimals, not rounded).
#     Prints a friendly message like:
#     "You exercised for 1.5 hours today. Keep it up, Joy!"

time_exercising = float(input("how many minutes did you exercise today: "))

hours = time_exercising / 60

print(f"You have exercised for {hours:.2f} hours. Keep it up, Joy!")