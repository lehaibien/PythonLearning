"""NUMBER GUESSING GAME
"""

import random

print("-" * 10 + "Number Guessing Game" + "-" * 10)
rngNumber = random.randint(1, 100)
while True:
    inp = int(input("Please guess a number: "))
    if inp == rngNumber:
        print("Correct!!! You win!!!")
        break
    elif inp > rngNumber:
        print("Your number is higher than our number")
    elif inp < rngNumber:
        print("Your number is lower than our number")
