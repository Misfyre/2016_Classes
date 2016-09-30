__author__ = "Nick Sarris (ngs5st)"

def grid_analysis():

    length_of_grid = int(input("What is the length of the list?: "))
    width_of_grid = int(input("What is the width of the list?: "))

    grid_dict = dict()
    for i in range(0, width_of_grid):
        grid_length = list('0' * length_of_grid)
        grid_length[i] = '1'
        grid_dict[i] = grid_length

    size_of_grid = length_of_grid * width_of_grid
    size_list = list(range(1, size_of_grid + 1))

    grid_location = int(input("Which square do you want to check?: "))
    column_location = grid_location // width_of_grid
    row_location = grid_location - (column_location * width_of_grid)
    check = (grid_dict[column_location][row_location - 1])

    if check == '0':
        return 'False'
    if check == '1':
        return 'True'

if __name__ == '__main__':
    result = grid_analysis()
    print ('')
    print (result)