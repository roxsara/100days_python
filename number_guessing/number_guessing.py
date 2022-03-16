from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    lives = 10
else:
    lives = 5

number = randint(1, 100)

guessed = False

while lives > 0 and not guessed:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        guessed = True
    else:
        lives -= 1
        if guess > number:
            print("Too high.")
        else:
            print("Too low.")
        print("Guess again")

if guessed:
    print(f"Congratulations!!! The number is indeed {number}")
else:
    print(f"Sorry, the number was {number}. Better luck next time!")