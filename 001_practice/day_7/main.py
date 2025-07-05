import random

# Step 5

# Import the word list from hangman_words.py
from hangman_words import word_list

# Import the logo and stages from hangman_arts.py
from hangman_arts import logo, stages

def play():
    chosen_word = random.choice(word_list).lower()
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6

    print(logo)

    # For testing: show the answer
    # print(f'Pssst, the solution is {chosen_word}.')

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    guessed_letters = []

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Check if letter already guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue
        else:
            guessed_letters.append(guess)

        # Check guessed letter
        if guess in chosen_word:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
        else:
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was '{chosen_word}'.")

        # Show current progress
        print(f"{' '.join(display)}")
        print(stages[lives])

        # Check win condition
        if "_" not in display:
            end_of_game = True
            print("You win!")
            print(f"The word was '{chosen_word}'.")

    playAgain()

def playAgain():
    answer = input("Do you want to play again? (Y/N): ").lower()
    if answer == "y":
        play()
    else:
        print("Thanks for playing!")
        exit()

play()
