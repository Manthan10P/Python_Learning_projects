import random  # Import the random module

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

attempts = 0  # Variable to count the number of attempts

# Loop until the player guesses correctly
while True:
    # Ask the user to guess the number
    guess = input("Guess a number between 1 and 100: ")

    # Check if the input is a valid number
    try:
        guess = int(guess)
    except ValueError:
        print("That's not a valid number. Please enter a number between 1 and 100.")
        continue  # If invalid input, ask again

    # Check if the guess is within the valid range
    if guess < 1 or guess > 100:
        print("Please guess a number between 1 and 100.")
        continue  # If out of range, ask again

    attempts += 1  # Increment attempts

    # Provide feedback to the player
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break  # Exit the loop to end the game
        else:
            random_number = random.randint(1, 100)  # Generate a new random number
            attempts = 0  # Reset attempts
