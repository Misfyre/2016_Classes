__author__ = "Nick Sarris (ngs5st)"

"""
Write a program to convert from Celsius to Fahrenheit:

You should prompt the user for the current temperature in Celsius,
then print out the corresponding temperature in Fahrenheit (recall
that 5(F − 32) = 9 C). An example run of the program might look like:
"""

def conversion():

        input_celsius = (input("What is the temperature in Celsius: "))
        output_fahrenheit = (float(input_celsius) * (9/5)) + 32
        return output_fahrenheit

output_fahrenheit = conversion()
print("It is %.01f degrees Fahrenheit" % output_fahrenheit)
