__author__ = "Nick Sarris"

def letter_to_index(letter):

    letter = letter.lower()
    alphabet_dict = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    if letter in alphabet_dict:
        return alphabet_dict.index(str(letter))
    else:
        return -1

def index_to_letter(index):

    try:
        index = int(index)
        alphabet_dict = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        return alphabet_dict[index]

    except ValueError:
        print('?')

def vigenere_encrypt(plain_letter, key_letter):

    try:
        plain_index = letter_to_index(plain_letter)
        key_index = letter_to_index(key_letter)
        cipher_index = plain_index + key_index

        if cipher_index >= 26:
            cipher_index = cipher_index - 26

        cipher_letter = index_to_letter(cipher_index)
        return cipher_letter

    except ValueError:
        return plain_letter

def vigenere_decrypt(cipher_letter, key_letter):

    try:
        cipher_index = letter_to_index(cipher_letter)
        key_index = letter_to_index(key_letter)
        plain_index = cipher_index - key_index

        if plain_index < 0:
            plain_index = plain_index + 26

        plain_letter = index_to_letter(plain_index)
        return plain_letter

    except ValueError:
        return cipher_letter

def encrypt(plaintext, key):

    try:
        plaintext_list = list(str(plaintext))
        key_list = list(str(key))
        ciphertext_list = []

        index = 0
        while len(key_list) < len(plaintext_list):
            list.append(key_list, key_list[index])
            index += 1

        for i in [i for i, x in enumerate(plaintext_list)]:
            plain_letter = plaintext_list[i].lower()
            key_letter = key_list[i].lower()

            try:
                final_letter = vigenere_encrypt(plain_letter, key_letter)
            except TypeError:
                final_letter = plain_letter

            list.append(ciphertext_list, final_letter)

        plaintext = ''.join(plaintext_list)
        cipherkey = ''.join(key_list)
        encrypted = ''.join(ciphertext_list)

        print ("Plaintexts: '%s'" % plaintext)
        print ("Encryptkey: '%s'" % cipherkey)
        print ("Ciphertext: '%s'" % encrypted)
        print ('')

    except ValueError:
        print('Query not understood. Sorry. Try again.')

def decrypt(ciphertext, key):

    try:
        ciphertext_list = list(str(ciphertext))
        key_list = list(str(key))
        plaintext_list = []

        index = 0
        while len(key_list) < len(ciphertext_list):
            list.append(key_list, key_list[index])
            index += 1

        for i in [i for i, x in enumerate(ciphertext_list)]:
            cipher_letter = ciphertext_list[i].lower()
            key_letter = key_list[i].lower()

            try:
                final_letter = vigenere_decrypt(cipher_letter, key_letter)
            except TypeError:
                final_letter = cipher_letter

            list.append(plaintext_list, final_letter)

        encrypted = ''.join(ciphertext_list)
        cipherkey = ''.join(key_list)
        plaintext = ''.join(plaintext_list)

        print ("Ciphertext: '%s'" % encrypted)
        print ("Decryptkey: '%s'" % cipherkey)
        print ("Plaintexts: '%s'" % plaintext)
        print ('')

    except ValueError:
        print('Query not understood. Sorry. Try again.')

