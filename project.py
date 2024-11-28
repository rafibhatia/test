from random import randint  # Import randint from the random module

secretNumber = randint(1, 30)  # Corrected the variable name
print('I am thinking of a number between 1 and 20.')
print(f"the number is {secretNumber}  ")

for guessesTaken in range(3):  # Changed range to 1, 4 to allow 3 guesses
    print('Take a guess.')
    guess = int(input('Pick a number between 1 and 20: '))

    if guess < secretNumber:
        print('Too low.')
    elif guess > secretNumber:
        print('Too high.')
    else:
        break  # Exit the loop if the guess is correct

if guess == secretNumber:
    print('Congratulations! You guessed the number.')
else:
    print('Sorry, try again tomorrow. The number was:')
