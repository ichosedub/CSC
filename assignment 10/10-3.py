from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)


from pathlib import Path

path = Path('pi_million_digits.txt')
contentss = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))


from pathlib import Path
path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, month/day/year: ")
if birthday in pi_string:
    print("Your birthday is in the first millon digits of pi!")
else:
    print("Your birthday is not in the first million digits of pi.")
