__author__ = "Nick Sarris (ngs5st)"

def create_book():

    dict_inputs = 5
    phone_book = dict()
    i = 0

    while i < dict_inputs:

        value = str(input("Add an entry to the phone book: "))
        final_value = value.split(' ')
        name = final_value[0]
        phone_number = final_value[1]
        phone_book[name] = phone_number

        i += 1

    print ('')
    name_to_use = (input("Who do you want to call?: "))

    if name_to_use in phone_book:
        print ("%s's number is: %s" % (name_to_use, phone_book[str(name_to_use)]))
        print ('')

    else:
        print("That name is not in the phone book.")
        print ('')

    number_to_use = input("What number do you want to lookup?: ")

    keys = list(phone_book.keys())
    values = list(phone_book.values())

    if number_to_use in values:
        index = values.index(number_to_use)
        key = keys[index]
        print ("That number belongs to: %s" % key)

    else:
        print ("That number is not in the phone book.")


create_book()