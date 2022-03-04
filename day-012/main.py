from random import randint
from os import system

def play_game():
    system("clear")
    print("Welcome to the Number Guessing Game!")
    
    chosen_number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    player_wins = False
    while lives > 0 and player_wins == False:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == chosen_number:
            player_wins = True
        elif guess > chosen_number:
            print("Too high")
            lives -= 1
        elif guess < chosen_number:
            print("Too low")
            lives -= 1
        
    if player_wins:
        print(f"You win! The number was {chosen_number}")
    else:
        print(f"You lose. The number was {chosen_number}")

    play_again = input("Play again? [y/N] ").lower()
    if play_again != "n":
        play_game()
        
play_game()
