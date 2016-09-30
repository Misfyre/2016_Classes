__author__ = "Nick Sarris"

def roman():

    roman_dict = dict()
    integers = ["3000","2000","1000","900","800","700","600","500","400","300",
                "200","100","90","80","70","60","50","40","30","20","10","9","8","7",
                "6","5","4","3","2","1","0"]
    roman_numerals = ["MMM","MM","M","CM","DCCC","DCC","DC","D","CD","CCC","CC",
                      "C","XC","LCCC","LCC","LC","L","XL","XXX","XX","X","IX","VIII",
                      "VII","VI","V","IV","III","II","I",""]

    while True:
        query = input("Do you want to use the RN Converter now? (Y,N): ")
        if query.upper() == 'Y':
            while True:
                try:
                    roman_input = input("Enter an Integer (1-3999): ")
                    for key,value in zip(integers, roman_numerals):
                        roman_dict[key] = value

                    processed_roman = []
                    roman_list = list(str(roman_input))
                    extra_zeros = len(roman_list)
                    try:
                        for i in roman_list:
                            extra_zeros = extra_zeros - 1
                            i = roman_dict[str(int(i)*(10**extra_zeros))]
                            list.append(processed_roman, i)
                        processed_roman = list(filter(None, processed_roman))
                        final_roman = "".join(processed_roman)
                        print ("In Roman Numerals, %s is %s" %(roman_input, final_roman))
                        print ('')
                        break

                    except ValueError:
                        print("Error. Your input does not fall within the given range (1-3999). Try again.")
                        print('')

                except KeyError:
                    print ("Error. Your input does not fall within the given range (1-3999). Try again.")
                    print('')

        while query.upper() not in ("Y, N"):
            print('Query not understood. Try again.')
            print('')
            query = "Y"

        if query.upper() == 'N':
            print('Thank you for your time. Ending the program now')
            break

if __name__ == "__main__":

    roman()