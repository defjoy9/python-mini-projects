# Ask the user to enter a sentence. Then:

#     Print how many words are in it.
#     Print the length of the longest word.
#     Print how many words have more than 5 letters.


sentence = input("Enter a sentence: ").split()

longest_word = ""
five_letters_more = 0
for word in sentence:
    if len(word) > len(longest_word):
        longest_word = word
    if len(word) > 5:
        five_letters_more += 1

print(f"""
      There are {len(sentence)} words in your sentence
      The longest word in your sentence is: '{longest_word}'
      There are {five_letters_more} words that have more than 5 letters    
""")