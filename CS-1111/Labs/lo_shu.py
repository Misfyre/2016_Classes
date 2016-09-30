__author__ = "Nick Sarris (ngs5st)"
import sys

def lo_shu():

    number_list = (input("Numbers: "))
    number_list = list(number_list.replace(' ',''))

    if len(number_list) != 9:
        sys.exit('You entered the wrong number of numbers!')

    index = 1
    length = 3

    print ('You entered: ')

    while index <= 3:
        value_list = []
        for i in range(index * int(((len(number_list)/3))) - length, index * int(((len(number_list)/3)))):
            list.append(value_list, number_list[i])

        output = ', '.join(map(str, value_list))
        output = output.replace(', ', ' ')
        print (output)
        index += 1

    row_1 = [number_list[0], number_list[1], number_list[2]]
    row_2 = [number_list[3], number_list[4], number_list[5]]
    row_3 = [number_list[6], number_list[7], number_list[8]]

    column_1 = [number_list[0], number_list[3], number_list[6]]
    column_2 = [number_list[1], number_list[4], number_list[7]]
    column_3 = [number_list[2], number_list[5], number_list[8]]

    diagonal_1 = [number_list[0], number_list[4], number_list[8]]
    diagonal_2 = [number_list[2], number_list[4], number_list[6]]

    key_list = ['Row 1', 'Row 2', 'Row 3', 'Column 1', 'Column 2', 'Column 3', 'Diagonal 1', 'Diagonal 2']
    value_list = [row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2]

    final_dict = dict()
    for key, value in zip(key_list, value_list):
        final_dict[key] = value

    error = False
    for key, value in final_dict.items():
        if int(value[0]) + int(value[1]) + int(value[2]) == 15:
            continue
        else:
            print (key, 'fails the test!')
            error = True

    if error == True:
        return ('This is not a Lo Shu Magic Square!')
    if error == False:
        return ('This is a valid Lo Shu Magic Square')

response = lo_shu()
print (response)