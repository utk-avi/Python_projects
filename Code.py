import random
def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
def check_winner(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"
def play_game():    
    choices = get_choices()
    result = check_winner(choices["player"], choices["computer"])
    return result 
if __name__ == "__main__":
    result = play_game()
    print(result)


    
# Rock, Paper, Scissors Game
