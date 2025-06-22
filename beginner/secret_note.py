# Asks the user to enter a message (a secret note 📜).
# Transforms the note using at least 4 different string methods before printing it.
# The final message must:

#     Be uppercased
#     Have all spaces replaced with underscores (_)
#     Be centered in a width of 50 characters (so it’s padded with spaces)
#     End with a single exclamation mark, even if the original input had none or too many.

secret_note = input("enter your secret note: ")
secret_note = secret_note.upper()
secret_note = secret_note.replace(" ", "_")
secret_note = secret_note.center(50)
secret_note = secret_note.replace("","!",-1)
print(secret_note)