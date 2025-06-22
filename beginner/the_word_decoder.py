# Write a program that:
#     Asks the user to enter a secret word or sentence.
#     Then extracts and displays:

#         The first character
#         The last character
#         The middle character (if the string has an odd number of characters)
#         Every second character in the string (starting from the first)

#     Make sure it handles both odd and even length strings!

secret_text = input("Enter a secret word or sentence: ")

print(f"First character: {secret_text[0]}")
print(f"Last character: {secret_text[-1]}")

if len(secret_text) % 2 == 1:
    middle_char = secret_text[len(secret_text) // 2]
else:
    mid = len(secret_text) // 2
    middle_char = secret_text[mid - 1] + secret_text[mid]
print(f"Middle character(s): {middle_char}")

print(f"Every second character: {secret_text[::2]}")