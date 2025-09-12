import random
answers = ["rock","paper", "scissors"]
computer_answer = random.choice(answers)
print("Do you want to play rock, paper, or scissors? OR quit?")
human_answer = input()
human_answer = human_answer.lower()

if human_answer not in answers:
    print("That's not a valid answer.")
    exit()
    
if computer_answer == human_answer:
    print("Nobody wins!")
elif computer_answer == "rock" and human_answer == "scissors":
    print("Computer wins")
elif computer_answer == "paper" and human_answer == "rock":
    print("Computer wins!")
elif computer_answer == "scissors" and human_answer == "paper":
    print("Coumpter wins!")
