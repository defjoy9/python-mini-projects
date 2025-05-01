def add():
    name = input("Enter name of the item you want to buy: ")
    price = float(input(f"Enter the price of {name}: "))
    cart.update({name: price})

def view():
    print("*******************************************")
    print("Your cart:")
    for key in cart.keys():
        print(key)

def checkout():
    total = 0
    print("*******************************************")
    print("Your cart")
    for key, value in cart.items():
        print(f"{key} - ${value}")
        total += value
    print(f"Your total is: ${total}")
cart = {}
is_running = True


print("Welcome to Joy's Store!")
add()

while is_running:
    print("*******************************************")
    print("You can now:\nPress 'a' to add another item\nPress 'v' to view your cart\nPress 'c' for checkout\nPress 'q' to quit")
    print("*******************************************\n\n")
    choice = input("I want to: ").lower()
    if choice == 'a':
        add()
    elif choice == 'v':
        view()
    elif choice == 'c':
        checkout()
        pay = input("type 'p' to pay: ").lower()
        if pay == 'p':
            is_running = False
        else:
            print("Invalid value")
    elif choice == 'q':
        print("Thank you for shopping with us!")
        is_running = False
    else:
        print("invalid choice, please try again.")
    
