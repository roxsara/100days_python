from art import logo, vs
from game_data import data
import random


def correct_answer(guess, first, second):
    """Checks if the answer is correct"""
    if first['follower_count'] > second['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'


second_element = random.choice(data)
on = True
score = 0
print(logo)

while on:
    first_element = second_element
    second_element = random.choice(data)
    while first_element == second_element:
        second_element = random.choice(data)
    print(f"Compare A: {first_element['name']}, a {first_element['description']}, from {first_element['country']}.")
    print(vs)
    print(f"Against B: {second_element['name']}, a {second_element['description']}, from {second_element['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if correct_answer(choice, first_element, second_element):
        score += 1
        print("Correct answer!")
    else:
        on = False
        print("Wrong answer!")
    print(f"Your score is {score}.")
