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
