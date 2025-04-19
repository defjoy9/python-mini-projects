# Goal: Create a timer that counts down from a given number of seconds and displays the time left.

import time

seconds = int(input("SET THE TIMER TO: "))

for i in range(seconds, 0, -1):
    print(f"{i} seconds left")
    time.sleep(1)
    
print("Time's up!")