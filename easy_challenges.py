# # Reverse a String - Ask the user for a word and print it in reverse using string indexing.


word = input("type a word: ")

print(word[::-1])

# Count Vowels in a Sentence - Ask for a sentence and count how many vowels (a, e, i, o, u) it contains.

sentence = input("type a sentence: ").lower()

vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0
}
for letter in sentence:
    if letter in vowels:
        vowels.update({letter: vowels.get(letter)+1})

print(vowels)

# Find the Maximum in a List - Ask for a list of numbers and find the largest number without using max().

numbers = input("give me a list of numbers: ").split()
max = numbers[0]


for digit in numbers:
    digit = int(digit)
    if digit >= max:
        max = digit
print(f"largest number is: {max}")

# Sum of Digits in a Number - Ask for a number and find the sum of its digits.

number = input("give me a number: ")
total = 0

for digit in number:
    digit = int(digit)
    total += digit

print(f"total is {total}")

