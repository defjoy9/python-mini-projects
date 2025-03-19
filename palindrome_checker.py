#Palindrome Checker - Ask the user for a word and check if it reads the same forward and backward.

word = input("enter a word: ").lower()


if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")