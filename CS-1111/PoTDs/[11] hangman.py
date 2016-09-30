__author__ = "Nick Sarris"

def initial_string(hidden_list):

    display_list = ["-"] * len(hidden_list)
    display_string = ''.join(display_list)
    return display_list, display_string

def update_string(input, hidden_list, display_list, tries):

    indices = [i for i, x in enumerate(hidden_list) if x == input]

    if not indices:
        tries = tries - 1

    for x in indices:
        display_list[x] = input

    display_string = ''.join(display_list)
    return hidden_list, display_list, display_string, tries

def hangman():

    while True:
        query = input("Would you like to play now? (Y,N): ")

        if query.upper() == "Y":
            tries = 6
            input_word = input("Enter a word: ")

            if input_word.isalpha():
                hidden_list = list(input_word.upper())
                display_list, display_string = initial_string(hidden_list)

                while True:

                    try:
                        new_letter = (input("[%s]: You have %i tries left. Please enter a letter now: " % (display_string, tries))).upper()
                        hidden_list, display_list, display_string, tries = update_string(new_letter, hidden_list, display_list, tries)

                        if display_string.count('-') == 0:
                            print ("[%s]: Congratulations! The word was '%s!'" % (display_string, input_word.upper()))
                            print ('')
                            break

                        if tries == 0:
                            print ("[%s]: Sorry, you lost. The word was '%s.'" % (display_string, input_word.upper()))
                            print ('')
                            break

                    except ValueError:
                        print('Query not understood. Try again.')
                        print('')

            else:
                print('Query not understood. Try again.')
                print('')

        while query.upper() not in ("Y, N"):
            print('Query not understood. Try again.')
            print('')
            query = "Y"

        if query.upper() == 'N':
            print('Thank you for your time. Ending the program now')
            break

hangman()

