#Digit Frequency Counter - Ask the user for a number and count how many times each digit appears.


number = input("enter a number: ")
count = [0,0,0,0,0,0,0,0,0,0]

for digit in number:
    
    count[int(digit)] +=1
print(count)

for x in range(len(count)):
    if count[x] == 0:
        continue
    print(f"digit {x}: {count[x]} times")