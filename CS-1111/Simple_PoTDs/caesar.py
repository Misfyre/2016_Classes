__author__ = "Nick Sarris"

def caesar(original_text):

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

    new_text = []
    split_text = list(original_text)

    for i in split_text:
        keys = list(caesar_dict.keys())
        values = list(caesar_dict.values())
        if i in values:
            index = values.index(i)
            key = keys[index]
            list.append(new_text, key)

    new_text = ''.join(new_text)
    return new_text

original_text = input("Enter your cipher text: ")
new_text = caesar(original_text)
print("Your decrypted phrase is: %s" % new_text)
