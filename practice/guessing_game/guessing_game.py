import random

def guessing_game():
    """
    Purpose: This is a guessing game to guess a hidden number.
    The user tries to guess a random number between 1 and 1000.
    The game provides feedback and updates the range dynamically with each guess.
    Maximum of 10 guesses allowed.
    """
    # Generate random number between 1 and 1000
    hidden_number = random.randint(1, 1000)

    min_range = 1
    max_range = 1000
    guess_count = 0
    max_guesses = 10
    
    print("\n----------Welcome to the Guessing Game!----------\n")
    print(f"I'm thinking of a number between {min_range} and {max_range}.")
    print(f"You have {max_guesses} guesses to find it!")
    print()
    
    while guess_count < max_guesses:
        try:
            # Prompt user for input with current range
            user_input = input(f"Enter your guess from {min_range} to {max_range}: ")

            # Handle empty input
            if not user_input:
                print("Please enter a number. Empty input is not allowed.")
                continue

            # Convert input to integer
            guess = int(user_input)
            guess_count += 1

            # Check if guess is within current range
            if guess < min_range or guess > max_range:
                print(f"Your guess must be between {min_range} and {max_range}.")
                guess_count -= 1  # Don't count this as a valid guess
                continue

            # Check if guess is correct
            if guess == hidden_number:
                print(f"You got it! The hidden number is {hidden_number}")
                print(f"It took you {guess_count} guess(es).")
                return

            # Provide feedback and update range
            if guess < hidden_number:
                print(f"Wrong! It's too low! Guess count: {guess_count}")
                min_range = guess + 1
            else:  # guess > hidden_number
                print(f"Wrong! It's too high! Guess count: {guess_count}")
                max_range = guess - 1

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        except KeyboardInterrupt:
            print("\nGame interrupted by user. Goodbye!")
            return

    # If we reach here, user has used all guesses
    print(f"Game over! You've used all {max_guesses} guess(es).")
    print(f"The hidden number is {hidden_number}.")

# Run the game
if __name__ == "__main__":
    guessing_game()