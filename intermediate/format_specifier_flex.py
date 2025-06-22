# Create a program that:

#     Asks the user for:
#         a product name,
#         a price (float),
#         and a quantity (int).
#     Calculates the total.
#     Displays a clean receipt like this:

# --------------------------
# Product:     Keyboard
# Price:       $49.99
# Quantity:    2
# --------------------------
# Total:       $99.98
# --------------------------

product = input("Enter a product name: ")
price = float(input("Enter a price: "))
quantity = int(input("Enter a quantity: "))

total = price * quantity

print("-" * 26)
print(f"{'Product:':<12}{product:>14}")
print(f"{'Price:':<12}{price:>13.2f}")
print(f"{'Quantity:':<12}{quantity:>14}")
print("-" * 26)
print(f"{'Total':<12}${total:>13.2f}")
print("-" * 26)