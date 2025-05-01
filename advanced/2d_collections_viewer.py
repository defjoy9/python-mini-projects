# simple program that lets the user explore a 2D list 

def actions(choice):
    match choice:
        case 1: #view row
            row = int(input("Which row would you like to view? (1-3): ")) - 1
            print(f"showing row {row}:\n{seats[row]}")
        case 2: #view column
            column = int(input("which column would you like to view? (1-3): "))
            column -= 1
            for row in seats:
                print(row[column], end=" ")
        case 3: #specific parameters
            parameters = input("enter two parameters (row,column): ").split(',')
            x = int(parameters[0])
            y = int(parameters[1])
            print(f"parameters for [{x},{y}] is: {seats[x][y]}")
        case _:
            print("invalid input")

seats = [
    ["Joy", "Alex", "Sam"],
    ["Luna", "Kai", "Eli"],
    ["Max", "Zoe", "Rin"]
]
is_runnning = True

# print the grid
for row in seats:
    for item in row:
        print(item, end=" ")
    print()
print()

while is_runnning:
    print("Press 1 to view row\nPress 2 to view column\nPress 3 to set specific parameters\nPress 'q' to quit\n")
    choice = input(": ")
    if choice == 'q':
        is_runnning = False
    else:
        choice = int(choice)
        actions(choice)