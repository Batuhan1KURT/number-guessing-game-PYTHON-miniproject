# Task: Number Guessing Game



import random  # Importing the random module

def main():  # Define the main function
    starter = 1  # Initialize the variable 'starter' to 1

    while starter:  # Start a loop, will run as long as 'starter' is truthy (non-zero)
        n = difficulty_selection(difficulty_choices())  # Call functions to set game difficulty
        actual_number = n[0]  # Extract the actual number from the returned list
        remaining_life = n[1]  # Extract remaining life from the returned list
        starter = 0  # Set 'starter' to 0, effectively ending the outer loop

        while remaining_life > 0:  # Another loop, will run as long as there are remaining lives
            guessed_number = getting_guess(getting_input(), actual_number)  # Get user's guess

            if guessed_number != actual_number:  # Check if the guess is incorrect
                remaining_life = lose_life(remaining_life)  # Decrement remaining life

            elif guessed_number == actual_number:  # Check if the guess is correct
                print("You won!")  # Print a win message
                print("Play again (1) or exit (2)?")  # Prompt user to play again or exit
                play_again = getting_input()  # Get user's choice

                if play_again == 1:  # If user chooses to play again
                    starter = 1  # Set 'starter' to 1, re-enter outer loop
                elif play_again == 2:  # If user chooses to exit
                    return  # Exit the program
                else:
                    print("Invalid input!")  # Print an error message for invalid input
                    return  # Exit the program

        if remaining_life == 0:  # If there are no remaining lives
            print("You lost!")  # Print a loss message
            print("Play again (1) or exit (2)?")  # Prompt user to play again or exit
            play_again = getting_input()  # Get user's choice

            if play_again == 1:  # If user chooses to play again
                starter = 1  # Set 'starter' to 1, re-enter outer loop
            elif play_again == 2:  # If user chooses to exit
                return  # Exit the program
            else:
                print("Invalid input!")  # Print an error message for invalid input
                return  # Exit the program

def getting_input():  # Define a function to get user input
    try:  # Try to execute the following code
        user_input = int(input("Enter: "))  # Prompt user for input and convert it to integer
        return user_input  # Return the user's input
    except ValueError:  # If a ValueError occurs (e.g., user input is not a number)
        print("Invalid input!")  # Print an error message
        return  # Return None

def difficulty_choices():  # Define a function for difficulty choices
    print("Enter (1) for hard difficulty, (2) for medium difficulty, or (3) for easy difficulty: ")  # Print instructions
    n = getting_input()  # Get user's choice of difficulty
    return n  # Return the user's choice

def difficulty_selection(n):  # Define a function to determine difficulty based on user's choice
    match n:  # Start a match statement
        case 1:  # If user chose 1
            return hard_difficulty()  # Return settings for hard difficulty
        case 2:  # If user chose 2
            return medium_difficulty()  # Return settings for medium difficulty
        case 3:  # If user chose 3
            return easy_difficulty()  # Return settings for easy difficulty
        case _:  # If user's choice doesn't match any case
            print(f"Invalid input! {n}")  # Print an error message
            return  # Return None

def hard_difficulty():  # Define a function for hard difficulty settings
    max_n = 100  # Set the maximum number for the game
    max_life = 3  # Set the maximum number of lives
    actual_number = randomizer(max_n)  # Generate a random number
    return [actual_number, max_life]  # Return a list with the random number and maximum lives

def medium_difficulty():  # Define a function for medium difficulty settings
    max_n = 50  # Set the maximum number for the game
    max_life = 4  # Set the maximum number of lives
    actual_number = randomizer(max_n)  # Generate a random number
    return [actual_number, max_life]  # Return a list with the random number and maximum lives

def easy_difficulty():  # Define a function for easy difficulty settings
    max_n = 20  # Set the maximum number for the game
    max_life = 5  # Set the maximum number of lives
    actual_number = randomizer(max_n)  # Generate a random number
    return [actual_number, max_life]  # Return a list with the random number and maximum lives

def randomizer(max_n):  # Define a function to generate a random number
    return random.randint(0, max_n)  # Generate and return a random integer between 0 and max_n

def lose_life(remaining_life):  # Define a function to decrement remaining life
    return remaining_life - 1  # Decrement and return the remaining life

def getting_guess(user_input, actual_number):  # Define a function to get the user's guess
    guess = user_input  # Assign user's input to 'guess'

    if guess < actual_number:  # If the guess is lower than the actual number
        print("Hint: The guess is lower than the selected number!")  # Print a hint message

    elif guess > actual_number:  # If the guess is higher than the actual number
        print("The guess is bigger than the selected number!")  # Print a message

    return guess  # Return the user's guess

if __name__ == "__main__":  # If this script is run directly
    main()  # Call the main function to start the game