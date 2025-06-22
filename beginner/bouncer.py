# Create a program that:

#     Asks the user for their age.
#     Asks the user if they’re on the guest list (yes or no).
#     Using logical operators:

#         If the person is 18 or older and on the guest list → print: "You're allowed in. Welcome!"
#         If the person is under 18 but on the guest list → print: "Sorry, you're too young to enter."
#         If the person is not on the guest list regardless of age → print: "Sorry, you're not on the list."

age = int(input("enter your age: "))
guest_list = input("are you on a gust list?(yes/no): ").strip().lower()

if age >= 18 and guest_list == "yes":
    print("You're allowed in. Welcome!")
elif age < 18 and guest_list == "yes":
    print("Sorry, you're too young to enter")
else:
    print("Sorry, you're not on the list")
