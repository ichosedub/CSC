from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user info if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path):
    """Get information from a new user."""
    username = input("name? ")
    game = input("favorite game? ")
    animal = input("favorite animal? ")

    user_dict = {
        'username': username,
        'game': game,
        'animal': animal,
    }

    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user by name, and state what we know about them."""
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome {user_dict['username']}!")
        print(f"you've been playing{user_dict['game']}. ")
        print(f"Have you seen a {user_dict['animal']}?")
    else:
        user_dict = get_new_user_info(path)
        msg = f"We'll remember you, {user_dict['username']}!"
        print(msg)

greet_user()