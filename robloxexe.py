# A>T
from random import randint
answer = randint(1, 100)
guess = -1
while guess != answer:
    print("Enter your guess")
    guess = input()
    guess = int (guess)
    if guess == answer:
        print("You figured it out")
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
print("game over")