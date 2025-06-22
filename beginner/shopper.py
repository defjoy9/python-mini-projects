# Create a program that:

#     Asks the user for the price of an item.
#     Asks how many items they want to buy.
#     Calculates the subtotal.
#     Adds 8% sales tax to the subtotal.

#     Displays:
#         The subtotal
#         The tax amount
#         The final total (all formatted to two decimal places)

item = input("What's the product you want to buy?: ")
price = float(input(f"What's the price of {item} (eg. 4.0): $"))
quantity = float(input(f"How many {item}'s would you like to buy: "))

subtotal = (price * quantity)
tax = subtotal * 0.08
total = subtotal + tax
print(f"Total is: {subtotal:.2f}")