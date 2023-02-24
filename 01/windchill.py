"""
This is a program that calculates windchill, based on a given temperature in
degrees Fahrenheit and a given wind speed in mph.

Written by Arka Rao
January 25th, 2016
"""

#Inform user of the intent of the program
#Ask user to input temperature in degrees Fahrenheit, which is stored
#Ask user to input wind speed in mph, which is stored
#Convert both T and W to float
#Calculate windchill via windchill formula, and store in a variable
#Convert windchill to float
#Tell user what the temperature feels like

print(" ")
print("This program calculates the 'wind chill' given the")
print("temperature and the wind speed.")
print(" ")
print("Please enter the current temperature in Fahrenheit, followed by")
print("the current wind speed in miles per hour.")
print(" ")

T = raw_input("Temperature (F): ")

W = raw_input("Wind Speed (mph): ")

T = float(T)
W = float(W)

windchill = 35.74 + (0.6215 * T) - 35.75 * (W**0.16) + 0.4275 * T * (W**0.16)

windchill = float(windchill)

print(" ")
print("What the temperature feels like:" + " " + str(windchill) + " " + "F")
print(" ")
