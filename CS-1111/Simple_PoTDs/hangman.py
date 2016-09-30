__author__ = "Nick Sarris"

def initial_string(hidden_list):

    display_list = ["-"] * len(hidden_list)
    display_string = ''.join(display_list)
    return display_list, display_string

def update_string(input, hidden_list, display_list, tries):

    indices = [i for i, x in enumerate(hidden_list) if x == input]

    if not indices:
        if tries != 1:
            print ("Incorrect!")
        tries = tries - 1

    correct_count = 1
    dash_count = display_list.count('-')

    for x in indices:
        display_list[x] = input
        while correct_count == 1 and dash_count > 1:
            print("Correct!")
            correct_count += 1


    display_string = ''.join(display_list)
    return hidden_list, display_list, display_string, tries

def hangman(input_word):

    tries = 6
    hidden_list = list(input_word.upper())
    display_list, display_string = initial_string(hidden_list)

    while True:

        new_letter = (input("[%s]: You have %i tries left. Please enter a letter now: " % (display_string, tries))).upper()
        hidden_list, display_list, display_string, tries = update_string(new_letter, hidden_list, display_list, tries)

        if display_string.count('-') == 0:
            print ("You win! The word was '%s!'" % (input_word.upper()))
            break

        if tries == 0:
            print ("You lose! The word was '%s.'" % (input_word.upper()))
            break


input_word = input("Enter a word: ")
hangman(input_word)

