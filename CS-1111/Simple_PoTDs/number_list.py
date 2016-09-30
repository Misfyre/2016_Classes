__author__ = "Nick Sarris (ngs5st)"

"""
Write a program called number_list.py that will read in 5 integer values from the user,
store them in a list, and perform some basic mathematical operations. Then, prompt the
user to remove one item and perform the same operations. You will need to calculate the
range (the difference between the largest and smallest numbers) and the average.
"""

def number_list():

    list_of_numbers = []
    length_of_list = 5

    try:

        for x in range(int(length_of_list)):
            continue

        for x in range(int(length_of_list)):
            value = int(input("Number %d: " % (x + 1)))
            list.append(list_of_numbers, value)
        print ('')

        average = (sum(list_of_numbers) / len(list_of_numbers))
        list_range = max(list_of_numbers) - min(list_of_numbers)

        print("You entered:", list_of_numbers)
        print("The average is: %.01f" % average)
        print("The range is: %d" % list_range)
        number_to_remove = int(input("Which item do you want to remove?: "))
        print ('')

        try:
            list_of_numbers.remove(number_to_remove)
            average = (sum(list_of_numbers) / len(list_of_numbers))
            list_range = max(list_of_numbers) - min(list_of_numbers)

            print("The new list has the following values:", list_of_numbers)
            print("The average is: %.01f" % average)
            print("The range is: %d" % list_range)

        except:
            print("Error... The number you tried to move is not in the list. Try again.")
            print('')

    except ValueError:
        print('Query not understood. Try again.')

number_list()
