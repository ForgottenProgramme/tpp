import random
import sys

choices= ["rock", "paper", "scissors"]
losses=0
wins=0
ties=0
print("ROCK, PAPER, SCISSORS")
print(f"Losses= {losses}, Wins= {wins}, Ties= {ties}")
while True:
    print("Choose 'Rock', 'Paper', 'Scissors' or 'Quit'.")
    user_choice= input()
    print(f"{user_choice} versus...")
    computer_choice= random.choice(choices)
    print(computer_choice)

    if user_choice=="quit":
        sys.exit()
    if user_choice==computer_choice:
        ties+=1
        print("It's a tie.")
    elif user_choice=="paper" and computer_choice=="rock" or user_choice=="scissors" and computer_choice=="paper" or user_choice=="rock" and computer_choice=="scissors":
        wins+=1
        print("You win!")
    else:
        losses+=1
        print("You lose!")
    
    print(f"Losses= {losses}, Wins= {wins}, Ties= {ties}")
    
    


