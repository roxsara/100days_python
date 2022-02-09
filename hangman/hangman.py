import random
from hangman_words import word_list
from hangman_art import stages, logo
# from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
#    clear()

    if guess in display:
      print(f'You have already guessed the {guess} letter! ')

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        lives -= 1
        print(f'The letter {guess} is not in the word. You lose a life!')
        if lives == 0:
            end_of_game = True
            print("You lost.")

    # Join all the elements in the list and turn it into a string
    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])