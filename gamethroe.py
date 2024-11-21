import random


doors = ["goat", "goat", "prize"]  
random.shuffle(doors)  


print("There are 3 doors. Behind one is a prize and behind the others are goats.")
print("Choose a door: 1, 2, or 3")

player_choice = input("Your choice: ")


player_choice = int(player_choice) - 1 



for i in range(3):
    if i != player_choice and doors[i] == "goat":
        revealed_door = i
        break

print(f"The host opens door {revealed_door + 1} to reveal a goat.")


switch = input("Do you want to switch to the other door? (yes or no): ").lower()


if switch == "yes":
    
    remaining_door = [0, 1, 2]
    remaining_door.remove(player_choice)
    remaining_door.remove(revealed_door)
    player_choice = remaining_door[0]


if doors[player_choice] == "prize":
    print("Congratulations! You won the prize!")
else:
    print("Sorry, you got a goat.")

