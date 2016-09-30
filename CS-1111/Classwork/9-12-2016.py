__author__ = "Nick Sarris (ngs5st)"

import random

def create_list():

    amount_of_numbers = int(input('How many Numbers do you want to Add?: '))

    number_list = []
    for i in range(amount_of_numbers):
        number = random.randint(1,100000)
        list.append(number_list, number)

    return number_list, max(number_list)

if __name__ == "__main__":

    number_list, max = create_list()

    print (number_list)
    print (max)