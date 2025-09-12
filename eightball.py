import random
answers = ["yes", "no", "maybe"]
print("What do you want to know?")
question = input()
answer = random.choice(answers)
print(answer)