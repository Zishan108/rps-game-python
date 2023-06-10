import random 

options = ["rock" , "paper" , "scissors"]

player_choice = input("Enter Your Choice(rock , paper , scissors): ")

computer_choice = random.choice(options)

print(f"computer chose {computer_choice}")

if computer_choice == player_choice :
    print("It's a Draw !!")
elif computer_choice == "rock" and player_choice == "paper" :
    print("You Won !!")
elif computer_choice == "paper" and player_choice == "rock" :
    print("You Lose !!")
elif computer_choice == "scissors" and player_choice == "rock" :
    print("You Won !!")
elif computer_choice == "rock" and player_choice == "scissors" :
    print("You Lose !!")
elif computer_choice == "paper" and player_choice == "scissors" :
    print("You Won !!")
elif computer_choice == "scissors" and player_choice == "paper" :
    print("You Lose !!")
    