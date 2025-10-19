answers ={}

polling_active = True

while polling_active:
    full_name = input("What is your full name?")
    vacation_area =input("What area would your like to vist?")

    answers[full_name] = vacation_area

    referral = input("Would you like to refer someone else to take this survey?(y/n)").strip().lower()
    if referral.lower() != 'y':
        polling_active = False

    print("\n Your Poll Results Are In")
    for full_name, vacation_area in answers.items():
        print(f"{full_name.title()} would wish to vist {vacation_area.title()}")




