"""
This is a program that asks the user for some text and a number, and displays
that text in the terminal window with a stair-like effect, using the inputted
number as a stopping point.

Written by Arka Rao
January 25th, 2016
"""
#Inform the user of the intent of the program
#Ask user to input a phrase, as well as a number, which are stored
#Convert stairnumber to int
#Create a forloop that induces the stair effect

print(" ")
print("This is a program that displays a phrase which you input with a")
print("stair like effect.")
print("You can also enter the number of stairs that you wish to see.")
print(" ")

text = raw_input("Text: ")
stairnumber = raw_input("Number of stairs: ")

stairnumber = int(stairnumber)

print(" ")
for i in range(0,stairnumber+1,1):
    print(" " * i + text)
print(" ")    
