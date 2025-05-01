

bill_amount = float(input("Bill Amount: $"))
tip = float(input("Tip (in %): "))
tip_amount = (tip * bill_amount) / 100.0
total = bill_amount + tip_amount

print(f"Bill Amount: ${bill_amount:.2f}")
print(f"Tip ({tip}%): ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")