__author__ = "Nick Sarris"

def credit_card():

    while True:
        query = input("Would you like to check your CC now? (Y,N): ")

        if query.upper() == "Y":
            try:
                input_card = input("Please enter your CC number now: ")
                cc_number = list(input_card)
                cc_length = len(cc_number) - 1
                other_length = len(cc_number) - 1

                every_other = 0
                remaining = 0
                every_other_list = []
                remaining_list = []

                while cc_length >= 0:
                    list.append(every_other_list, cc_length)
                    every_other += int(cc_number[cc_length])
                    cc_length = cc_length - 2

                while other_length >= 0:
                    if other_length not in every_other_list:
                        list.append(remaining_list, (2*(int((cc_number[other_length])))))
                    other_length = other_length - 1

                for i in remaining_list:
                    for ch in str(i):
                        remaining += int(ch)

                final_check = every_other + remaining
                if final_check % 10 == 0:
                    print ("Yes, %s is a valid credit card number" % input_card)
                    print ('')

                else:
                    print ("No, %s is not a valid credit card number" % input_card)
                    print ('')

            except ValueError:
                print ("Query not understood. Try again.")
                print ('')

        while query.upper() not in ("Y, N"):
            print('Query not understood. Try again.')
            print('')
            query = "Y"

        if query.upper() == 'N':
            print('Thank you for your time. Ending the program now')
            break

if __name__ == "__main__":

    credit_card()