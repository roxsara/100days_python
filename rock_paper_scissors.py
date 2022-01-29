# 100 days of code - python bootcamp udemy
# Project 4

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

computer_choice = random.randint(0, 2)

options = [rock, paper, scissors]

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice < computer_choice or (user_choice == 2 and computer_choice == 0):
    print("You lost!")
else:
    print('You won!')

print(options[user_choice])
print(options[computer_choice])