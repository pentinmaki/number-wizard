import random

def play_game():
    print("Welcome to Number Wizard!")
    print("I'm thinking of a number between 1 and 100...")

    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} tries.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_game()
