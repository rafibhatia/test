import random


def play_monty_hall(switch_choice):
    
    doors = ["goat", "goat", "prize"]
    random.shuffle(doors)  

    
    player_choice = random.randint(0, 2)  

    
    for i in range(3):
        if i != player_choice and doors[i] == "goat":
            revealed_door = i
            break


    if switch_choice:
        
        remaining_door = [0, 1, 2]
        remaining_door.remove(player_choice)
        remaining_door.remove(revealed_door)
        player_choice = remaining_door[0]

    
    if doors[player_choice] == "prize":
        return 1 
    else:
        return 0 


def run_simulation(num_games, switch_choice):
    wins = 0
    for _ in range(num_games):
        wins += play_monty_hall(switch_choice)
    return wins


num_games = 100
switch_wins = run_simulation(num_games, switch_choice=True)  # Wins when switching
stay_wins = run_simulation(num_games, switch_choice=False)  # Wins when not switching


print(f"Results after {num_games} games:")
print(f"Wins when switching: {switch_wins} out of {num_games}")
print(f"Wins when not switching: {stay_wins} out of {num_games}")


print(f"Win percentage when switching: {switch_wins / num_games * 100}%")
print(f"Win percentage when not switching: {stay_wins / num_games * 100}%")
