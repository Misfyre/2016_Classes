__author__ = "Nick Sarris (ngs5st)"

def edit_string():

    original_string = list(input("What is the original string?: "))
    substring = input("What part of the original string do you want to remove?: ")

    count = 0
    new_string = []

    for i in original_string:
        if i not in substring:
            list.append(new_string, i)

    return new_string

if __name__ == '__main__':

    for y in range(0, -22, -2):
        print(y)