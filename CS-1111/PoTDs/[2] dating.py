__author__ = "Nick Sarris (ngs5st)"

"""
Sorry, TA. I wrote this like a month ago when I found all the old
PoTDs on the old CS1111 site. Started from the basic template and went from there.
I got bored and didn't want to submit something so basic. I made sure that the program should
account for any input using try/except syntax, and turned it into an infinite loop until manually
stopped by a specific input. If the auto-checker isn't sophisticated enough to deal with it and crashes,
my bad. Let me know and I'll rewrite the other 15 PoTDs.

Write a program that uses a folk rule to tell you the age range of people you can date.

There is a folk rule that says you can date people as young as half your age plus seven
years old. This suggests they can date you if they are as old as twice your age minus
thirteen.
"""

def dating_rule(input_age):

    try:
        low_end = (int(input_age) / 2) + 7
        high_end = (int(input_age) * 2) - 13
        print ("You can date people between %d and %d years old" % (low_end, high_end))

    except ValueError:
        print('Query not understood. Try again.')

if __name__ == "__main__":

    while True:
        query = input("Do you want to use the program now? (Y, N): ")

        if query.upper() == "Y":
            input_age= input("How old are you?: ")
            dating_rule(input_age)
            print ('')
        elif query.upper() == "N":
            print('Thank you for your time. Ending the program now')
            break
        else:
            print('Query not understood. Try again.')
            print('')
