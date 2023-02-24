"""
# horserace.py

This program simulates a race between four horses which is driven by
random forwards movement for each horse per a time step. When a horse passes
distance = 75, he has crossed the finish line, and the race ends.

Written by Arka Rao
February 17, 2016
"""
#import random
#create horselist, empty horse strings
#create list of horseinfo
#set variable with bool for while loop to run smoothly
#simulate race with while loop
#end while loop by using bool variable to end
#at end, print "we have a winner!"

"""
I was not able to get the horserace to run with a delay. After some research,
I learned that this can be done via the use of the class "time" - however, I
do not know how to do that yet.
"""

from random import *

def main():
    horse = ['1:','2:','3:','4:']
    letter = 'H'
    horse1 = ''
    horse2 = ''
    horse3 = ''
    horse4 = ''
    horseinfo = [horse1,horse2,horse3,horse4]
    distance = 0
    raceOver = False
    while not raceOver:
        for i in range(len(horse)):
            print horse[i] + horseinfo[i] 
            rnum = randrange(1,6)
            horseinfo[i] = horseinfo[i]+(rnum*letter)
            distance = len(horseinfo[i])
            if distance > 75:
                raceOver= True
        print("-"*75)
    print("We have a winner!")
        
main()
