import random
import time


name = input("enter your name: ")
number = input("pick a number between 1 and 5: ")

fortunes = {
    1: f"Today is your lucky day {name} — but only if you wear socks that match.",
    2: f"Beware of ducks {name}. That’s all I’ll say",
    3: f"Success is in your future {name}… after a nap",
    4: f"Someone is thinking of you {name}. Probably your computer.",
    5: f"Fortune not found {name}. Try again later."
}
fortune_choice = random.randint(1,5)

print("thinking...")
time.sleep(2)


print("Your Fortune:")
print(f"{fortunes.get(fortune_choice)}")