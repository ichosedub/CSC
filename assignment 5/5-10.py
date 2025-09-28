old_users = ['Admin', 'david', 'adrien', 'kyle', 'mark']
new_users = ['James', 'marty', 'linda','jacob','adam']

current_users = [user.lower() for user in old_users]

for new_user in new_users:
    if new_user.lower() in current_users:
     print(f"Sory current username '{new_user} is already taken.")
    else:
       print(f"The username '{new_user} is currently available.")