"""
# Put your top-down design for the two-dice pig game here.
This is a top-down design for the game two-dice pig. I first stubbed out all the functions I
intended to use, and later added all the code in. The file twodicepig.py will contain the same
code/comments, but has a more detailed explanation of the program's intent.

Written by Arka Rao
March 22nd, 2016
"""

"""
Below are the original two-dice pig design comments. I didn't alter them in order to accurately
reflect my thought process in the original design.
"""

#import random
#print intro
#establish accumulator variables
#pass those through to print first game scoreboard
#in while true loop..
#get the player's score by using a function specific to the player's turn
#Within that, call roll function and score function. Return that turn's score
#total score by adding that turn score to it, however account for reverting to 0 with dummy value
#print computer intro message, pass for now
#give the computer a turn, same procedure
#print special, specific computer message - pass for now
#print gamescoreboard
#repeat until someone wins

from random import *

def main():
    printIntroduction()
    playerTotal = 0
    computerTotal = 0
    printScoreBoard(playerTotal,computerTotal)
    while True:

        playerScore = playerTurn()
        if playerScore == "q":
            print("Okay, we'll play again sometime!")
            break
        if playerScore == -2:
            playerTotal = 0
        else:
            playerTotal += playerScore

        computerScore = computerTurn()
        if computerScore == -2:
            computerTotal = 0
        else:
            computerTotal += computerScore

        printScoreBoard(playerTotal,computerTotal)

        if computerTotal >= 100 or playerTotal >= 100:
            print("Game over! Let's play again sometime.")
            break
    
def printIntroduction():
    """
    This function will print the rules and an encouraging message at the start.
    """
    print("")
    print("****Two-Dice Pig****")
    print("Let's play two-dice pig! Read the rules below.")
    print("1. To win, you have to get to 100 or above.")
    print("2. On your turn, roll the two dice repeatedly until either")
    print("a 1 is rolled, or you decide to 'hold'.")
    print("3. if you decide to 'hold', your turn total is added to your game total")
    print("for the two rolled dice".)
    print("")
    print("If neither die shows a 1, their sum is added to your turn total.")
    print("If a single 1 is rolled, your turn ends, and your turn total is zero for that round.")
    print("If double-1's are rolled, your entire game total is reset to zero and your turn ends. ")
    print("")
    print("Ready to play? Good luck!")

def printScoreBoard(playerTotal,computerTotal):
    """
    This function will print the initial scoreboard using the initial, unchanged accumulator
    variables.
    """
    print("")
    print("="*42)
    print("player total = %d computer total = %d"%(playerTotal,computerTotal))
    print("="*42)
    print("")
    
def playerTurn():
    """
    This function takes no values. It first rolls two dice using the roll function, then passes
    that variable (the dice are stored in a list assigned to a variable) through the score
    function to obtain the player's score. It then returns that score.
    """
    turnTotal = 0

    while True:
        choice = validInput()
        if choice == "r":
            outcome = roll()
            print("Roll: " + str(outcome))
            playerScore = score(outcome)
            if playerScore == -2:
                print("Your score was reset!")
                return playerScore
            elif playerScore == 0:
                print("Turn: %d" %(playerScore))
                return playerScore
            else:
                turnTotal += playerScore
                print("Turn: %d" %(turnTotal))
        elif choice == "h":
            print("Your score this round was %d" %(turnTotal))
            return turnTotal
        else:
            return choice
            
def computerTurn():
    """
    This function takes no values. It first rolls two dice using the roll function, then passes
    that variable (the dice are stored in a list assigned to a variable) through the score
    function to obtain the computer's score. It then returns that score.
    """
    print("")
    prompt = "*"*20
    exclamation = " my turn!!!!"
    print(str(prompt)+str(exclamation))
    turnTotal = 0

    while True:
        outcome = roll()
        print("Turn: " + str(outcome))
        computerScore = score(outcome)

        if computerScore == -2 or computerScore == 0:
            computerMessage(computerScore)
            return computerScore
        else:
            turnTotal += computerScore

        if turnTotal >= 20:
            computerMessage(turnTotal)
            return turnTotal
        
def roll():
    """
    This function takes no values and simulates the rolling of two dice, stores the values of both
    in a list, and returns the list.
    """
    diceOne = randrange(1,7,1)
    diceTwo = randrange(1,7,1)
    ls = [diceOne,diceTwo]
    return ls
    
def score(outcome):
    """
    This function takes the list with the two dice values from roll and returns values for the
    score.
    A dummy value was assigned in order to account for the special rule of the score resetting to
    0 when two 1s are rolled.
    """
    if outcome[0] == 1 and outcome[1] == 1:
        return -2
    elif outcome[0] == 1 or outcome [1] == 1:
        return 0
    else:
        total = outcome[0] + outcome[1]
        return total

def computerMessage(computerScore):
    """
    This function will print special messages from the computer after its turn is complete, based
    on the current total score after the turn.
    """
    if computerScore == -2:
        print("Oh dear...")
    elif computerScore >= 20:
        print("I'll stick with that!")
    else:
        print("Bleh... thats okay.")

def validInput():
    while True:
        try:
            choice = raw_input("Roll(r),Hold(h),Quit(q): ")
        except ValueError:
            print("Please enter either r, h, or q")

        if choice == "r" or choice == "h" or choice == "q":
            return choice
        else:
            print("Please enter either r, h, or q")
            pass

main()
