# Keyword Arguments Exercise - Write a function that takes a name and an optional greeting message (defaulting to "Hello"). 
#                              It should print the greeting followed by the name. 
#                              Call the function in different ways using keyword arguments.


def greeting(name, greet="Hello"):
    return print(greet, name)

greeting("joy")
greeting("joy","Welcome back,")

# exercise 2 - Challenge: Describe a Person

def describe_person(*args, **kwargs):
    print("Hobbies:", ", ".join(args))
    
    print("Details: ")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")



describe_person("reading","gaming",age=25,city="New York")

# .join() exercises

# combine words
words = ["i","am","bad","at","coding"]

print(" ".join(words))

# comma-separated list

fruits = ["apple", "banana", "cherry"]

print(", ".join(fruits))

# acronym generator
words = "World Health Organization".split()
print(words)
first_letters = [word[0] for word in words] 
print(first_letters)
acronym = ''.join(first_letters)
print(acronym)


#reverse sentence order
word = "Hello world this is Python".split()
word = reversed(word)
print(" ".join(word))

#dash-separated string
print("1, 2, 3, 4, 5".replace(', ','-'))