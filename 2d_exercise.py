# exercise 1

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print 2d list normally
for item in numbers:
    print(item)

#print only the first row
for item in numbers[0]:
    print(item)

#print the number in the middle (5)
print(numbers[1][1])

# exercise 2 - sum of all numbers in 2d list
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0
for row in numbers:
    for item in row:
        total += item

print(f'total is {total}')

# exercise 3 - find the Largest Number in a 2D List
numbers = [
    [3, 8, 1],
    [12, 7, 9],
    [5, 15, 4]
]
max_number = numbers[0][0]
for row in numbers:
    for item in row:
        if item > max:
            max_number = item

print(max_number)

# exercise 4 Count Even and Odd Numbers in a 2D List

numbers = [
    [10, 3, 5],
    [8, 12, 7],
    [6, 9, 2]
]
even_num = 0
odd_num = 0
for row in numbers:
    for number in row:
        if number % 2 == 0:
            even_num += 1
        else:
            odd_num += 1
print(f"odd numbers: {odd_num}, even numbers {even_num}")