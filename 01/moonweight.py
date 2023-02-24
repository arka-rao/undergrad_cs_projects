"""
This is a program that asks for the user's weight and calculates its
equivalent on the moon.

Written by Arka Rao
January 25th, 2016
"""
#Inform user of the intent of the program
#Ask the user to enter their weight, which is stored as a variable
#Convert weight variable to a float for further operations
#Create variable that accounts for the weight conversion between earth and moon
#Convert moonweight from int to float
#Print the user's weight on the Moon

print(" ")
print("This program calculates what you weigh on the Moon.")
print("Please enter your weight on the Earth.")
print(" ")

earthweight = raw_input("Earth weight (lbs): ")

earthweight = float(earthweight)

moonweight = earthweight/6.0

moonweight = float(moonweight)

print("On the Moon, you would weigh" + " " + str(moonweight) + " " + "lbs.")
print(" ")
