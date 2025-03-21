#Pascal's Triangle Generator - Ask the user for a number n, then generate the first n rows of Pascal's Triangle.

triangle = []
rows = int(input("Enter number of rows: "))

triangle.append([1])  # First row
if rows > 1:
    triangle.append([1, 1])  # Second row

for i in range(2, rows):  # Start from row 2
    prev_row = triangle[i - 1]  # Get the previous row
    new_row = [1]  # Start new row with 1

    for j in range(len(prev_row) - 1):  # Generate middle elements
        new_row.append(prev_row[j] + prev_row[j + 1])

    new_row.append(1)  # End row with 1
    triangle.append(new_row)  # Add to triangle

for row in triangle:
    print(" ".join(map(str, row)))  # Print neatly
    #print(row)