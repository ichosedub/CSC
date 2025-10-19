active = True
while active:
    pizza_topping = input("Enter a pizza topping (or 'quit' to stop): ")

    if pizza_topping == 'quit':
        active = False
    else:
        print(f"You added {pizza_topping} to your pizza!")