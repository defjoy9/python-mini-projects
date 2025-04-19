# Goal: Create a program that checks if someone is old enough to watch certain types of movies.

age = input("enter your age: ")

while not age.isdigit():
    age = input("age invalid!, please enter your age: ")

age = int(age)


if age <= 7:
    print("You can watch G-rated movies only")
elif age>7 and age<=12:
    print("You can watch PG movies")
elif age>12 and age<=16:
    print("You can watch PG-13 movies")
elif age>16 and age<=18:
    print("You can watch R-rated movies")
elif age>18:
    print("You can watch all movies, including NC-17")
