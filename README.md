# Number Guessing Game

A simple Python game where the user guesses a random number between two user-defined values within a limited number of attempts.

---

## Features
- Validates user input for numbers and range.
- Tracks remaining attempts.
- Provides feedback on whether the guess is too high, too low, or correct.
- Handles invalid inputs gracefully (non-integer values, reversed ranges).
- Reveals the correct number if all attempts are exhausted.

---

## How to Use

1. **Run the Script**:
   ```bash
   python number_guessing_game.py

   Enter the Range:

2. **Input two integers to define the range (e.g., 10 and 20).**

## Guess the Number:

You have 5 attempts to guess the correct number.

After each guess, the program will tell you if your guess is too high, too low, or correct.

## Error Handling
Invalid Input: If you enter a non-integer value for the range or guess, the program will prompt you to enter a valid number.

Invalid Range: If the first number is greater than or equal to the second, the program will exit immediately.

## Example Usage
Scenario 1: Correct Guess
Please enter your first number: 
1
Please enter your second number:
10
You have 5 attempts left. Guess a number between 1 and 10: 5
Your guess is greater than my number. Try again...
You have 4 attempts left. Guess a number between 1 and 10: 3
You Win!


## Scenario 2: All Attempts Exhausted

Please enter your first number: 
1
Please enter your second number:
10
You have 5 attempts left. Guess a number between 1 and 10: 8
Your guess is greater than my number. Try again...
You have 4 attempts left. Guess a number between 1 and 10: 4
Your guess is less than my number. Try again...
You have 3 attempts left. Guess a number between 1 and 10: 5
Your guess is greater than my number. Try again...
You have 2 attempts left. Guess a number between 1 and 10: 3
Your guess is less than my number. Try again...
You have 1 attempts left. Guess a number between 1 and 10: 2
Your guess is less than my number. Try again...
Sorry, you've used all 5 attempts. The correct number was 6.

# Code Explanation
## Dependencies
Requires Python 3.x and the random module (part of the standard library).

## Key Components
Input Validation:

Uses try-except blocks to handle non-integer inputs for the range and guesses.

Checks if the range is valid (min_number < max_number).

## Game Logic:

Generates a random integer within the user-defined range using random.randint().

Uses a while loop to give the user 5 attempts.

Compares the guess with the random number and provides feedback.

Exits the loop early if the guess is correct.

## User Feedback:

Shows remaining attempts dynamically (max_attempts - counter).

Prints the correct number if all attempts are used.

# Run the Game
Clone the repository or copy the code into a file named guess_number_game.py and run:
python guess_number_game.py

# Enjoy the game! 🎮