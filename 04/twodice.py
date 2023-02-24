"""
# twodice.py
This program simulates the game Two-Dice Pig - a variation on the game Pig. It
employs the use of two functions, roll (to simulate rolling the dice), score
(to calculate and return the score of the two dice, based on the rules), and
a while loop in main to run the game according to specified parameters.

Written by Arka Rao
February 20, 2016
"""
#import random
#def main
#part A - create function to roll dice, return result
#part B - create score function to sum score within parameters, return this
#within score, assign arbitrary number to ensure score can be run in while
#part C - create while loop in main, with accumulators and specific parameters

from random import *

def main():
    totalscore = 0
    count = 0
    while totalscore <= 100:
            result = roll()
            totalscore += score(result)
            count+=1
            if score(result) == -2:
                totalscore = 0
            print("%s. %s score = %s "%(count,result,totalscore))

def roll():
    one = randrange(1,7,1)
    two = randrange(1,7,1)
    L =[one,two]
    return(L)

"""
When I ran the program, I noticed that sometimes [1,1] wouldn't revert the sum
to 0. I fixed this by assigning a number to return when the numbers both came
out as 1, and then had that overwrite the accumulator in the main loop to
successfully revert the sum to 0. This has worked every time so far.
"""

def score(L):
    if L[0]== 1 and L[1] ==1:
        return -2
    elif L[0]==1 or L[1]==1:
        return 0
    else:
        score = L[0] + L[1]
        return score
    


main()
