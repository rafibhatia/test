import random

# Function to simulate one game of Monty Hall
def play_monty_hall(switch_choice):
    # Set up the doors with one prize and two goats
    doors = ["goat", "goat", "prize"]
    random.shuffle(doors)  # Shuffle to randomize where the prize is

    # Player makes an initial choice (randomly picking one door)
    player_choice = random.randint(0, 2)  # Random choice between 0, 1, 2

    # Host reveals a goat behind one of the doors the player didn't pick
    for i in range(3):
        if i != player_choice and doors[i] == "goat":
            revealed_door = i
            break

    # If the player decides to switch, choose the other remaining door
    if switch_choice:
        # Get the remaining door after removing the player's choice and the revealed goat
        remaining_door = [0, 1, 2]
        remaining_door.remove(player_choice)
        remaining_door.remove(revealed_door)
        player_choice = remaining_door[0]

    # Check if the player wins the prize
    if doors[player_choice] == "prize":
        return 1  # Win
    else:
        return 0  # Loss

# Function to run the game multiple times
def run_simulation(num_games, switch_choice):
    wins = 0
    for _ in range(num_games):
        wins += play_monty_hall(switch_choice)
    return wins

# Run the simulation for 100 games
num_games = 100
switch_wins = run_simulation(num_games, switch_choice=True)  # Wins when switching
stay_wins = run_simulation(num_games, switch_choice=False)  # Wins when not switching

# Show the results
print(f"Results after {num_games} games:")
print(f"Wins when switching: {switch_wins} out of {num_games}")
print(f"Wins when not switching: {stay_wins} out of {num_games}")

# Calculate and show the win percentage
print(f"Win percentage when switching: {switch_wins / num_games * 100}%")
print(f"Win percentage when not switching: {stay_wins / num_games * 100}%")
