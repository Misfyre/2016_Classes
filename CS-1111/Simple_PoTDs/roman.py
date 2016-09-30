__author__ = "Nick Sarris"

def roman():

    roman_dict = dict()
    integers = ["3000","2000","1000","900","800","700","600","500","400","300","200","100",
                "90","80","70","60","50","40","30","20","10","9","8","7","6","5","4","3","2","1","0"]
    roman_numerals = ["MMM","MM","M","CM","DCCC","DCC","DC","D","CD","CCC","CC","C","XC","LXXX",
                      "LXX","LX","L","XL","XXX","XX","X","IX","VIII","VII","VI","V","IV","III","II","I",""]

    for key, value in zip(integers, roman_numerals):
        roman_dict[key] = value

    processed_roman = []
    roman_list = list(str(roman_input))
    extra_zeros = len(roman_list)

    for i in roman_list:
        extra_zeros = extra_zeros - 1
        i = roman_dict[str(int(i) * (10 ** extra_zeros))]
        list.append(processed_roman, i)

    processed_roman = list(filter(None, processed_roman))
    final_roman = "".join(processed_roman)

    return roman_input, final_roman

roman_input = input("Enter an Integer (1-3999): ")

if int(roman_input) >= 1 and int(roman_input) <= 3999:
    roman_input, final_roman = roman()
    print("In roman numerals, %s is %s" % (roman_input, final_roman))

else:
    print("Input must be between 1 and 3999")