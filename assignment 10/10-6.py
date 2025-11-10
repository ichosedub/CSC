try:
    x = input("insert a numberr: ")
    x = int(x)

    y = input("insert another number: ")
    y = int(y)
except ValueError:
    print("no number inserted.")
else:
    sum = x + y
    print(f"{x} plus {y} is {sum}.")