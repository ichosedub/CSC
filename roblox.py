# A>T
from random import randint
answer = randint(1, 100)

while True:
    print("Enter your guess")
    guess = input()
    guess = int (guess)
    if guess == answer:
        print("You figured it out")
        break
    if guess > answer:
        print("Too high")
    if guess < answer:
        print("Too low")
print("game over")
