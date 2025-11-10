print("Enter 'q' to quit.\n")

while True:
    try:
        x = input("\nenter a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("enter another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("what is entered is not a number.")

    else:
        sum = x + y
        print(f"{x} plus {y} is {sum}.")