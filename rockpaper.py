import random
def get_choices():
    player_choice = input("Enter your choices(rock, paper, scissor): ")
    list= ["rock", "paper", "scissor"]
    computer_choice = (random.choice(list))
    choices = { "player": player_choice, "computer": computer_choice}
    return choices

def winner(player, computer):
    if player == computer:
        return "It's tie, Play again!"
    elif player == "paper":
        if computer == "rock":
            return "You Win!"
        else:
            return "You Loss!"
    elif player == "rock":
        if computer == "scissor":
            return "You Win!"
        else:
            return "You Loss!"    
    elif player == "scissor":
        if computer == "paper":
            return "You Win!"
        else:
            return "You Loss!"
result = get_choices()
final_result = winner(result["player"], result["computer"])
print(f"You chose: {result["player"]}")
print(f"Computer chose: {result["computer"]}")
print(final_result)