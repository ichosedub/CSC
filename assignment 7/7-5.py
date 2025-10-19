while True:
    age = input("How old are you? (enter 'quit' now to stop)")

    if age == 'quit':
        break

    inserted_age = int(age)
    if inserted_age < 3:
        print("Your ticket is free of charge")
    elif inserted_age <= 12:
        print("You must simply pay 10$")
    else:
        if inserted_age >= 12:
            print("Your ticket costs 15$ since you're older")