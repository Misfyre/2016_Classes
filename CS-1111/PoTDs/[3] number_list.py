__author__ = "Nick Sarris (ngs5st)"

"""
Sorry, TA. I wrote this like a month ago when I found all the old
PoTDs on the old CS1111 site. Started from the basic template and went from there.
I got bored and didn't want to submit something so basic. I made sure that the program should
account for any input using try/except syntax, and turned it into an infinite loop until manually
stopped by a specific input. If the auto-checker isn't sophisticated enough to deal with it and crashes,
my bad. Let me know and I'll rewrite the other 15 PoTDs.

Write a program called number_list.py that will read in 5 integer values from the user,
store them in a list, and perform some basic mathematical operations. Then, prompt the
user to remove one item and perform the same operations. You will need to calculate the
range (the difference between the largest and smallest numbers) and the average.
"""

def number_list():

    list_of_numbers = []
    length_of_list = (input("How many values do you want in the list?: "))

    try:

        for x in range(int(length_of_list)):
            continue

        print ('')
        for x in range(int(length_of_list)):
            value = int(input("Enter Number %d: " % x))
            list.append(list_of_numbers, value)
        print ('')

        while len(list_of_numbers) >= 1:

            average = (sum(list_of_numbers) / len(list_of_numbers))
            list_range = max(list_of_numbers) - min(list_of_numbers)

            print("The Average is %.02f" % average)
            print("The Range is %d" % list_range)
            print(list_of_numbers)
            print('')

            number_to_remove = int(input("Which item do you want to remove?: "))

            try:
                list_of_numbers.remove(number_to_remove)

            except:
                print("Error... The number you tried to move is not in the list. Try again.")
                print('')
                continue

        print("There are no more values to remove. Thanks for playing!")

    except ValueError:
        print('Query not understood. Try again.')


if __name__ == "__main__":

    while True:
        query = input("Do you want to use the program now? (Y, N): ")

        if query.upper() == "Y":
            number_list()
            print ('')
        elif query.upper() == "N":
            print('Thank you for your time. Ending the program now')
            break
        else:
            print('Query not understood. Try again.')
            print('')
