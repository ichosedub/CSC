username_input = []

for users in username_input:
    if users == 'admin':
        print("Hello admin, would you like to recieve a status report?")
    else:
        print(f"Hello {users}, welcome back.")
else:
    print("Waiting for user input")