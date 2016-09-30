__author__ = "Nick Sarris"

def syllables(input_word):

    letter_list = list(input_word)
    vowel_list = ["a", "e", "i", "o", "u", "y"]
    syllable_counter = 0

    if letter_list[-1] == "e":
        letter_list.pop(-1)

    word_length = len(letter_list)
    drop_list = []
    length = 0

    while length < word_length:
        letter_1 = letter_list[length]
        if letter_1 in vowel_list:
            syllable_counter += 1
            list.append(drop_list, letter_1)
            while True:
                try:
                    length += 1
                    letter_1 = letter_list[length]
                    if letter_1 in vowel_list:
                        list.append(drop_list, letter_1)
                        continue
                    else:
                        break
                except IndexError:
                    break
        else:
            length += 1

    print (drop_list)

    for i in drop_list:
        letter_list.remove(i)

    if syllable_counter == 0:
        syllable_counter = 1

    return syllable_counter

input_word = input("Please enter your word now: ")
syllable_counter = syllables(input_word)
print("The word %s has %s syllables." % (input_word, syllable_counter))
