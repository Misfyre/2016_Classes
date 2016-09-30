__author__ = "Nick Sarris (ngs5st)"
import random

def responses():

    """Generates random response based on input added in response_values and a random number related to the len of
    response_values. If necessary to add more responses, simply add them to the end of response_values and the program
    should take care of it."""

    #Responses gathered from https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers

    response_values = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.",
                     "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.",
                     "Yes.", "Signs point to yes.", "Reply hazy try again.", "Ask again later.",
                     "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                     "Don't count on it.", "My reply is no.", "My sources say no.","Outlook not so good.",
                     "Very doubtful"]

    response_keys = list(range(0, len(response_values)))
    random_number = random.randint(0,19)
    response_dict = {}

    for key, value in zip(response_keys, response_values):
        response_dict[key] = value

    response = response_dict[random_number]
    return response

if __name__ == "__main__":

    while True:
        query = input("Do you want to use the program now? (Y, N): ")

        if query.upper() == "Y":
            input_question = input("What question do you wish to ask the 8 ball?: ")
            print ("You asked the 8 ball: %s" % input_question)
            answer = responses()
            print (answer)
            print ('')

        elif query.upper() == "N":
            print('Thank you for your time. Ending the program now')
            break

        else:
            print('Query not understood. Try again.')
            print('')
