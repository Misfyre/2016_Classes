__author__ = "Nick Sarris (ngs5st)"

"""
Write a program that uses a folk rule to tell you the age range of people you can date.

There is a folk rule that says you can date people as young as half your age plus seven
years old. This suggests they can date you if they are as old as twice your age minus
thirteen.
"""

def dating_rule(input_age):

    low_end = (int(input_age) / 2) + 7
    high_end = (int(input_age) * 2) - 13
    return low_end, high_end

input_age= input("How old are you? ")
low_end, high_end = dating_rule(input_age)
print("You can date people between %d and %d years old" % (low_end, high_end))
