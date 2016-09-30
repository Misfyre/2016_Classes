__author__ = "Nick Sarris"
import random

def generate_number():

    print ('Initializing Game. You have 5 Guesses:')
    while True:

        input_number = input("What Should The Answer Be? (1-100)(-1 for Random): ")

        if int(input_number) == -1:
            input_number = random.randint(1,100)
            print('')
            return int(input_number)
        if 0 < int(input_number) < 100:
            print('')
            return int(input_number)

        if int(input_number) < -1:
            print("The Number does not Fall Within the Given Range. Try Again.")
        if int(input_number) > 100:
            print("The Number does not Fall Within the Given Range. Try Again.")
        if int(input_number) == 0:
            print("The Number does not Fall Within the Given Range. Try Again.")

def higher_lower(input_number):

    i = 0
    while i < 5:
        try:
            guess = int(input("Guess a Number: "))
            if guess > input_number:
                print ("The Number is Lower than That.")
                i += 1
            elif guess < input_number:
                print ("The Number is Higher than That.")
                i += 1
            elif guess == input_number:
                print ('')
                print ("Congratulations! You win!")
                break
        except:
            print ("The Value Entered is not a valid Integer. Try again.")

    if i == 5:
        print ('')
        print ("Sorry! You Lose. The number was %i." % input_number)

if __name__ == "__main__":

    input_number = generate_number()
    higher_lower(input_number)