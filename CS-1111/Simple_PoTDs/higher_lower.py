__author__ = "Nick Sarris"
import random

"""
Write a program to play a simple guessing game with you.

The computer will pick a number between 1 and 100, then give you 5 guesses.
If you guess right, it will say “You win!”. If you guess higher or lower
than correct, it will say “The number is higher than that.” (or lower).
If after five guesses they still don’t know the number, print “You lose;
the number was x.” where x was the number you were to guess.

Before the game begins, ask what number to pick. If they say “−1”,
pick randomly; otherwise, use their number even if it is outside the 1–100
range. Check your notes for how to get a random integer by using the
random.randint() method.
"""

def generate_number():

    input_number = input("What should the answer be? ")

    if int(input_number) == -1:
        input_number = random.randint(1,100)
        return int(input_number)
    else:
        return int(input_number)

def higher_lower(input_number):

    i = 0

    while i < 5:
        guess = int(input("Guess a number: "))

        if guess > input_number:
            print ("The number is lower than that.")
            i += 1
        elif guess < input_number:
            print ("The number is higher than that.")
            i += 1
        elif guess == input_number:
            print ("You win!")
            break

    if i == 5:
        print ("You lose; the number was %i." % input_number)

input_number = generate_number()
higher_lower(input_number)