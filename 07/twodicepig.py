"""
#twodicepig.py
This is a program that allows the user to play a game of two-dice pig with
the computer. The user is first introduced to the intent of the program. From
there, the user is taught all the rules of two-dice pig, and is then allowed
to play the game against the computer. There are several functions that allow
the user to repeatedly play the game (in rounds) until they win or the
computer wins. These functions correct for valid input as well as generate
simulated "computer turns" with corresponding messages, as if the computer
was a real player.

Written by Arka Rao
March 22nd, 2016
"""

"""
Below are the pseudocode comments for my final version of twodicepig. 
"""

#import random
#print introduction
#establish accumulator variables
#pass those through to print first game scoreboard
#in while true loop..
#get the player's score by using a function specific to the player's turn
#Within that, call roll function and score function. Return that turn's score
#total score by adding that turn score to it, however account for reverting to 0 with dummy value
#make sure to allow the player to roll repeatedly, roll, or quit
#make sure that input is valid with a validinput function of some kind
#print computer intro message
#give the computer a turn, same procedure
#print special, specific computer messages
#the computer repeatedly rolls until its total is >= 20, upon which point it holds
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
    print("3. if you decide to 'hold', your turn total is added to your game\
total")
    print("for the two rolled dice.")
    print("")
    print("If neither die shows a 1, their sum is added to your turn total.")
    print("If a single 1 is rolled, your turn ends, and your turn total is zero for")
    print("that round.")
    print("If double-1's are rolled, your entire game total is reset to zero and your")
    print("turn will end.")
    print("")
    print("Ready to play? Good luck!")

def printScoreBoard(playerTotal,computerTotal):
    """
    This function will print the scoreboard using the specified accumulator
    variables.
    """
    print("")
    print("="*42)
    print("player total = %d computer total = %d"%(playerTotal,computerTotal))
    print("="*42)
    print("")
    
def playerTurn():
    """
    This function takes no values. It allows the player to get a turn in
    twodicepig. An accumulator is first established, and
    then the user is given options to choose from (in validInput). They can
    roll as many times as they want, until they roll a
    one. Their score is updated according to the rules, and the function
    returns either the accumulator, the dummy value, or a
    sum of zero based on the outcome of their roll. If in validInput they
    select "h", the accumulator (which is their turn
    total) is returned. If in validInput, they choose to quit, the string 'q'
    is returned, which signals main to break.
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
            print("Your score this round was held at %d" %(turnTotal))
            return turnTotal
        else:
            return choice
            
def computerTurn():
    """
    This function takes no values. It first prints the computer's intro
    message. It then establishes
    an accumulator for the computer's turn. In the while loop, the computer
    rolls the dice and gets
    a subsequent score. If the score is either the dummy value or 0, an
    appropriate message is printed,
    and that score is returned. Otherwise, the total score for the turn is
    updated. Once the turn total
    is >= 20, the computer ceases to roll the dice and holds that sum.
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
    This function takes no values and simulates the rolling of two dice,
    stores the values of both in a list, and returns the list.
    """
    diceOne = randrange(1,7,1)
    diceTwo = randrange(1,7,1)
    ls = [diceOne,diceTwo]
    return ls
    
def score(outcome):
    """
    This function takes the list with the two dice values from roll and
    returns values for the score.
    A dummy value was assigned in order to account for the special rule of
    the score resetting to 0 when two 1s are rolled.
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
    This function will print special messages from the computer after its
    turn is complete, based on the given score from the score function. If
    the computer rolls two ones, it prints a certain message. If the computer
    rolls a single 1, it prints a different message. If the computer has
    rolled successfully to the point where its turn total is >= 20, then it
    prints a third type of message.
    """
    if computerScore == -2:
        print("Oh dear...")
    elif computerScore >= 20:
        print("I'll stick with that!")
    else:
        print("Bleh... thats okay.")

def validInput():
    """
    This function takes no values and asks the user for input during their
    turn in the game. It corrects for value errors, and input that isn't "r",
    "h", or "q". It then returns their choice.
    """
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
