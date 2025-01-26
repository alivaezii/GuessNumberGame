import random

try:
    # Ask the user for the range
    min_number = int(input("Please enter your first number: \n"))
    max_number = int(input("Please enter your second number:\n"))

    # Ensure min_number is less than max_number
    if min_number >= max_number:
        print("The first number must be less than the second number.")
        exit()  # Exit the program if the range is invalid

except ValueError:
    print("Please enter valid numbers.")
    exit()  # Exit the program if input is invalid

# Generate a random number within the range
random_number = random.randint(min_number, max_number)

# Counter for attempts
counter = 0
max_attempts = 5

while counter < max_attempts:
    try:
        # Ask the user to guess the number
        guess_number = int(input(f"You have {max_attempts - counter} attempts left. Guess a number between {min_number} and {max_number}: "))

        # Validate if the guess is within the range
        if guess_number < min_number or guess_number > max_number:
            print(f"Your guess is not valid! It must be between {min_number} and {max_number}.")
            continue  # Skip the rest of the loop and prompt again

        # Check the guess
        if guess_number == random_number:
            print("You Win!")
            break  # Exit the loop if the guess is correct
        elif guess_number > random_number:
            print("Your guess is greater than my number. Try again...")
        else:
            print("Your guess is less than my number. Try again...")

        counter += 1  # Increment the attempt counter

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# If the loop ends without guessing correctly
if counter == max_attempts:
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {random_number}.")