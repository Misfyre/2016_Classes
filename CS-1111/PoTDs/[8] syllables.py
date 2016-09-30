__author__ = "Nick Sarris"

def syllables():

    while True:
        query = input("Would you like to use the syllable counter now? (Y,N): ")

        if query.upper() == "Y":
            input_word = input("Please enter your word now: ")
            letter_list = list(input_word)

            if ' ' not in letter_list:
                try:
                    vowel_list = ["a", "e", "i", "o", "u", "y"]
                    syllable_counter = 0

                    if letter_list[-1] == "e":
                        letter_list.pop(-1)

                    word_length = len(letter_list)
                    drop_list = []
                    length = 0

                    while (length + 1) < word_length:
                        letter_1 = letter_list[length]
                        letter_2 = letter_list[length + 1]
                        if letter_1 in vowel_list and letter_2 in vowel_list:
                            syllable_counter += 1
                            list.append(drop_list, letter_1)
                            list.append(drop_list, letter_2)
                        length += 1

                    for i in drop_list:
                        letter_list.remove(i)

                    for i in letter_list:
                        if i in vowel_list:
                            syllable_counter += 1
                            letter_list.remove(i)

                    if syllable_counter == 0:
                        syllable_counter = 1

                    print ("Your word, '%s', has %s syllables." % (input_word, syllable_counter))
                    print ('')

                except ValueError:
                    print("Query not understood. Try again.")
                    print('')
            else:
                print("Query not understood. Try again.")
                print('')

        while query.upper() not in ("Y, N"):
            print('Query not understood. Try again.')
            print('')
            query = "Y"

        if query.upper() == 'N':
            print('Thank you for your time. Ending the program now')
            break

if __name__ == "__main__":

    syllables()