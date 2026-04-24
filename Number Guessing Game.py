# NumberGuessingGame.py
import random

def is_same(target, number):
    if target == number:
        result = "Win"
    elif target > number:
        result = "High"
    else:
        result = "Low"
    return result

while True:
    computer_number = random.randint(1, 100)
    print("Hello. I have thought of a number between 1 and 100.")

    guess = int(input ("Can you guess it in under 6 attempts?"))
    guesses = 1

    higher_or_lower = is_same(guess, computer_number)

    while higher_or_lower != "Win" and guesses < 6:
        if higher_or_lower == "Low":
            guess = int(input("Too low. Try again."))
        else:
            guess = int(input("Too high. Try again."))
        higher_or_lower = is_same(guess, computer_number)
        guesses += 1

    if higher_or_lower == "Win":
        input("Correct! Well done. Press ENTER to restart.")
    else:
        input("Out of guesses! The number was {}. Press ENTER to restart.".format(computer_number))