__author__ = "Nick Sarris"

def caesar():

    keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            " ", "'",",",".","!","?","@","#","$","%","^","&","*",
            "(",")","1","2","3","4","5","6","7","8","9","0","-",
            "+","=","~","`","|","/",";",":","[","]","{","}"]

    values = ["d","e","f","g","h","i","j","k","l","m","n","o","p",
              "q","r","s","t","u","v","w","x","y","z","a","b","c",
              "D","E","F","G","H","I","J","K","L","M","N","O","P",
              "Q","R","S","T","U","V","W","X","Y","Z","A","B","C",
              " ", "'",",",".","!","?","@","#","$","%","^","&","*",
              "(",")","1","2","3","4","5","6","7","8","9","0","-",
              "+","=","~","`","|","/",";",":","[","]","{","}"]

    caesar_dict = dict()
    for key,value in zip(keys, values):
        caesar_dict[key] = value

    while True:
        query = input("Would you like to use the cipher now? (Y,N): ")

        if query.upper() == 'Y':
            type_of_use = input("What do you want to do? (Encrypt, Decrypt): ")

            if type_of_use.lower() == 'encrypt':
                try:
                    new_text = []
                    original_text = input("Enter your text to encrypt: ")
                    split_text = list(original_text)
                    for i in split_text:
                        i = caesar_dict[i]
                        list.append(new_text, i)
                    new_text = ''.join(new_text)
                    print ("Your encrypted phrase is: %s" % new_text)
                    print ('')
                except KeyError:
                    print ("Error. Your input is not recognized. Try again.")
                    print ('')

            elif type_of_use.lower() == 'decrypt':
                try:
                    new_text = []
                    original_text = input("Enter your text to decrypt: ")
                    split_text = list(original_text)
                    for i in split_text:
                        keys = list(caesar_dict.keys())
                        values = list(caesar_dict.values())
                        if i in values:
                            index = values.index(i)
                            key = keys[index]
                            list.append(new_text, key)
                    new_text = ''.join(new_text)
                    print("Your decrypted phrase is: %s" % new_text)
                    print('')
                except KeyError:
                    print("Error. Your input is not recognized. Try again.")
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

    caesar()