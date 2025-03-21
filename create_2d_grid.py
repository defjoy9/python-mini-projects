#Challenge: Create a 2D Grid - task: Ask the user for two numbers: rows and columns. Then, create a 2D list (grid) where each element is 0, and print it neatly.

rows = int(input('how many rows: '))
columns = int(input("how many columns: "))


grid = []

for i in range(rows):
    row = []
    for j in range(columns):
        row.append(0)
    grid.append(row)


for row in grid:
    print(" ".join(map(str, row)))