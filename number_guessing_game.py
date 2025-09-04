import random

def number_guessing_game():
    # Randomly select a number between 1 and 50
    computer = random.randint(1, 50) 
    attempts_left = 5

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print(f"You have {attempts_left} attempts to guess it.")

    # Loop for the number of attempts
    while attempts_left > 0:
        try:
            # Ask the user for their guess
            guess = int(input(f"\nAttempt {6 - attempts_left}: Enter your guess: "))

            # Check if the guess is valid (within the range)
            if guess < 1 or guess > 50:
                print("Please guess a number between 1 and 50.")
                continue

            # Check if the guess is correct
            if guess == computer: 
                print(f"Congratulations! You've guessed the correct number: {computer}") 
                break
            elif guess < computer:
                print("Too low!")
            else:
                print("Too high!")

            # Reduce the number of attempts left
            attempts_left -= 1

            # If no attempts are left, reveal the correct number
            if attempts_left == 0:
                print(f"\nGame over! The correct number was {computer}.")

        except ValueError:
            print("Invalid input! Please enter a number.")

# Run the game
number_guessing_game()
