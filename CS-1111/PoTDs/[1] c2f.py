__author__ = "Nick Sarris (ngs5st)"

"""
Sorry, TA. I wrote this like a month ago when I found all the old
PoTDs on the old CS1111 site. Started from the basic template and went from there.
I got bored and didn't want to submit something so basic. I made sure that the program should
account for any input using try/except syntax, and turned it into an infinite loop until manually
stopped by a specific input. If the auto-checker isn't sophisticated enough to deal with it and crashes,
my bad. Let me know and I'll rewrite the other 15 PoTDs.

Write a program to convert from Celsius to Fahrenheit:

You should prompt the user for the current temperature in Celsius,
then print out the corresponding temperature in Fahrenheit (recall
that 5(F − 32) = 9 C). An example run of the program might look like:
"""

def conversion(type_of_conversion):

    if str(type_of_conversion).upper() == "F TO C":
        input_fahrenheit = (input("What is the Temperature in Fahrenheit: "))

        try:
            output_celsius = (float(input_fahrenheit) - 32) * (5/9)
            print ("It is %.01f degrees Celsius" % output_celsius)
        except ValueError:
            print ("Error: Your temperature input was not an integer. Try again.")

    elif str(type_of_conversion).upper() == "C TO F":
        input_celsius = (input("What is the Temperature in Celsius: "))

        try:
            output_fahrenheit = (float(input_celsius) * (9/5)) + 32
            print ("It is %.01f degrees Fahrenheit" % output_fahrenheit)
        except ValueError:
            print ("Error: Your temperature input was not an integer. Try again.")

    else:
        print ("Error: Your input was not a valid conversion. Try again.")

if __name__ == "__main__":

    while True:
        query = input("Do you want to use the program now? (Y, N): ")

        if query.upper() == "Y":
            type_of_conversion = input("What type of conversion? (F to C, C to F): ")
            conversion(type_of_conversion)
            print ('')
        elif query.upper() == "N":
            print('Thank you for your time. Ending the program now')
            break
        else:
            print ('Query not understood. Try again.')
            print ('')

