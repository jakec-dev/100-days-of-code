import random
from hangman_art import logo, stages
from hangman_words import word_list
from os import system

lives = 6
end_of_game = False

chosen_word = random.choice(word_list)
display = []
for _ in chosen_word:
    display.append('_')
guessed_letters = []

print(logo)

while not end_of_game:
    print(stages[lives])
    print(f"{' '.join(display)}\n")
    guess = input("Guess a letter: ").lower()
    system('clear')

    if guess in guessed_letters:
        print(f"You have aleady guessed '{guess}'. Try again.")
    else:
        guessed_letters.append(guess)

        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
       
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word was {chosen_word}")
        
        if "_" not in display:
            end_of_game = True
            print("You win!")
        