import random
import os

def main():
    play_again = 'y'
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's play a game.")

    while play_again.lower() == 'y':
        play_game(name)
        play_again = input("\nDo you want to play again? (y/n): ")

def play_game(name):
    num_chances_input = input("Enter the number of chances (default 15): ")
    if num_chances_input == "":
        num_chances = 15
    else:
        num_chances = int(num_chances_input)
        if num_chances < 1 or num_chances > 100:
            print("Invalid input. Setting number of chances to default (15).")
            num_chances = 15

    n = random.randint(1, 200)
    good_guesses = 0
    error_guesses = 0
    guess_count = 0

    while guess_count < num_chances:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print(f"Guesses left: {num_chances - guess_count}")
        print(f"Number of guesses made: {guess_count}")
        print()
        guess_str = input("Enter an integer from 1 to 200 (or 'q' to quit): ")

        if guess_str.lower() == 'q':
            print("Quitting the game.")
            break

        try:
            guess = int(guess_str)
            if guess < 1 or guess > 200:
                raise ValueError("Invalid input. Enter a number between 1 and 200.")
        except ValueError as e:
            print(e)
            error_guesses += 1
            continue

        guess_count += 1

        if guess < n:
            print("\nGuess is LOW.")
        elif guess > n:
            print("\nGuess is HIGH.")
        else:
            good_guesses += 1
            print(f"\nCongratulations, {name}! You guessed the number {n} in {guess_count} guesses.")
            break
    else:
        print(f"\nYou lost, {name}. You ran out of chances. The number was {n}.")

    print(f"Number of good guesses: {good_guesses}")
    print(f"Number of error guesses: {error_guesses}")

main()
