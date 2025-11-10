from pathlib import Path

path = Path('guest_book.txt')

prompt = "\nWhats your name?\nEnter 'quit' if you're done:"

guest_names = []
while True:
    name = input(prompt)
    if name.strip().lower() == 'quit':
        break
    print(f"Thanks {name}, I'll add you to the guest book.")
    guest_names.append(name)

file_string = '\n'.join(guest_names) + '\n'
for name in guest_names:
    file_string += f"{name}\n"

path.write_text(file_string)