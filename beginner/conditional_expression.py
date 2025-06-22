# Create a program that:

#     Asks the user for their age.
#     Use a single line of code with a conditional expression to assign a message:

#         If they’re 18 or older, the message should be: "You’re eligible for a fast pass!"
#         Otherwise, it should be: "Standard entry only."

#     Then, print that message.


age = int(input("enter your age: "))
print("You're eligible for a fast pass!" if age >= 18 else "Standard entry only")