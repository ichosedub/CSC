word = "PYTHON"

scrambled = ["_" for letter in word]
print("".join(scrambled))
print("Guess a letter.")
guess = input()
guess = guess.upper()
if guess in word:
    letter_index = word.index(guess)
    secret[letter_index] = guess
else:
    print("Not in word.")
    print("".join(scrambled))

while True:
    print("Guess a letter.")
    guess = input()
    guess = guess.upper()
    if guess in word:
        letter_index = word.index(guess)
        scrambled[letter_index] = guess
    else:
        print("Not in word.")
    print("".join(scrambled))
    
