"""
# candyhearts.py
This program will randomly generate a set of 5 "candyheart" messages from a
preset list of messages. It relies on a function within main to operate.

Written by Arka Rao
February 16th, 2016
"""
#import random
#inform user of the program's function
#def main, write forloop
#def candyheart, create list and use "choice" to pick random message
#return that random message to forloop of def main
#print 5 random messages via forloop

from random import *

def main():
    print("")
    print("This program will generate 5 random"\
          " candyheart messages from a preset list.")
    print("")
    for i in range(6):
        print candyheart()
        print("")

def candyheart():
    messages = ["Wink\nWink","All\nMine!","Forever\nYours","My\nBaby",
                "Love\nYou!"]
    randmsg = choice(messages)
    return randmsg 

main()
