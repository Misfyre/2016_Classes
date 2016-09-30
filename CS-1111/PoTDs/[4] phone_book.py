__author__ = "Nick Sarris"

def create_book():

    try:
        dict_inputs = int(input("How many entries to you want to add?: "))
        phone_book = dict()
        i = 0
        while i < dict_inputs:
            value = str(input("Add an entry to the Phone Book: "))
            final_value = value.split(' ')
            try:
                name = final_value[0].capitalize()
                phone_number = final_value[1]
                number_check = phone_number.split('-')
                for x in number_check:
                    if x.isdigit():
                        phone_book[name] = phone_number
                    else:
                        print ("Error... That number is not valid. Try again.")
                i += 1
            except IndexError:
                print ("Error... You did not add a number or you did not enter a valid number. Try again.")
        print ('')
        print ('Thank you. All entries have been added to the phone book.')
        while True:
            query = input("Do you want to use the phone book now? (Y,N): ")
            if query.upper() == 'Y':
                type_of_use = input("What do you want to look up? (Name, Number): ")
                if type_of_use.lower() == 'name':
                    name_to_use = (input("Who would you like to look up?: ")).capitalize()
                    try:
                        print ("%s's number is %s" % (name_to_use, phone_book[str(name_to_use)]))
                        print ('')
                    except KeyError:
                        print ("That name is not in the phone book. Try again.")
                        print ('')
                elif type_of_use.lower() == 'number':
                    number_to_use = input("What number would you like to look up?: ")
                    keys = list(phone_book.keys())
                    values = list(phone_book.values())
                    if number_to_use in values:
                        index = values.index(number_to_use)
                        key = keys[index]
                        print ("That number belongs to: %s" % key)
                        print ('')
                    else:
                        print ("That number is not in the phone book. Try again.")
                        print ('')
                else:
                    print ("Query not understood. Try again.")
                    print ('')
            while query.upper() not in ("Y, N"):
                print ('Query not understood. Try again.')
                print ('')
                query = "Y"
            if query.upper() == 'N':
                print('Thank you for your time. Ending the program now')
                break
    except ValueError:
        print("Error... You did not add a number. Ending the program now.")

if __name__ == "__main__":

    create_book()