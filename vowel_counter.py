#  Ask the user for a sentence and count how many vowels (a, e, i, o, u) are in it.


vowels = {"a", "e", "i", "o", "u"}
sentence = input("enter a sentence: ")
sentence = sentence.lower()
count = 0


for letter in sentence:
    if letter in vowels:
        count += 1

print(f"your sentence has {count} vowels")