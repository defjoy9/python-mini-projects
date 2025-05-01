# Unique Character Counter - Ask the user for a sentence and count how many unique characters (excluding spaces) it contains.

sentence = input("enter a sentence: ")

used_letters = set()

for character in sentence:
    if character !=" ":
        used_letters.add(character)

print(f"unique characters: {len(used_letters)}")