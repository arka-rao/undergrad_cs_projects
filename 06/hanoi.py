"""
# hanoi.py
This program simulates the famous puzzle "Towers of Hanoi" and allows the user
to play it. They can specify the number of disks (from 1 to 100) that they
want to play with, and the program will ask them which disk they'd like to
move and where to move it to. It will overwrite and print three "rods" until
the user has effectively solved the puzzle. Initially, a test function was
called to run one test iteration of the code, which uses several functions.
From there, a while loop was implemented in main with a similar layout as
test. It allows the user to repeatedly play the game (while correcting for
invalid moves) until they win, upon which a congratulatory message is
displayed on screen.

Written by Arka Rao
March 03, 2016
"""

def main():
    #step1
    #test()

    #main - ask user for number of disks
    print("")
    ndisks = getInt("How many disks do you want?: ",1,100)
    print("")

    #main - create initial puzzle configuration
    ls = range(ndisks,0,-1)
    rod1 = ls
    rod2 = []
    rod3 = []
    print("")
    print("This is the starting position! Good luck!")
    print("")
    print(rod1)
    print(rod2)
    print(rod3)

    #main - build the loop
    while True:
        #game over check
        print("")
        status = isGameOver(rod1,rod2,rod3)
        if status == True:
            print("Congratulations! You won.")
            print("")
            break
        else:
            #ask user for a valid disk to move
            disk = getValidMove(ndisks,rod1,rod2,rod3)
            #ask user for rod to move it to
            rodnum = getValidRod(disk,rod1,rod2,rod3)
            #move the disk
            move(disk,rodnum,rod1,rod2,rod3)
            #print game state
            printState(rod1,rod2,rod3)
            
def test():
    #test-step2
    print("in getInt")
    ndisks = getInt("How many disks do you want?: ",1,100)
    print("%d is the number of disks"%(ndisks))

    #test-step3
    print("in diskMovable")
    ls = range(ndisks,0,-1)
    rod1 = ls
    rod2 = []
    rod3 = []
    print(rod1)
    print(rod2)
    print(rod3)
    result = diskMovable(ndisks,rod1,rod2,rod3)
    print("can it be moved?: %s "%(result))

    #test-step4
    print("in getValidMove")
    valid = getValidMove(ndisks,rod1,rod2,rod3)
    print("is it a valid move?: %s"%(valid))

    #test-step5
    print("in checkRod")
    disk = ndisks
    rod = []
    check = checkRod(disk,rod)
    print("is it open? %s"%(check))
    print("The first time, it will run checkRod blankly.")

    #test-step6
    print("in getValidRod")
    validrod = getValidRod(disk,rod1,rod2,rod3)
    print(validrod)

    #test-step7
    print("in move")
    rodnum = validrod
    shift = move(1,rodnum,rod1,rod2,rod3)
    print(shift)

    #test-step8
    print("Game status: ")
    status = isGameOver(rod1,rod2,rod3)
    print(status)

    #test-step9
    printState(rod1,rod2,rod3)
    
def getInt(prompt,low,high):
    """
    This function takes a prompt string and two integers between the preset min
    and max. While correcting for ValueErrors, it asks the user for a number
    of discs. If the number is valid, it returns it.
    """
    while True:
        try:
            number = int(raw_input(prompt))
        except ValueError:
            print("Please enter an integer between %d and %d"%(low,high))

        if number >= low and number <= high:
            return number
        else:
            print("Please enter an integer between %d and %d"%(low,high))

def diskMovable(disk,rod1,rod2,rod3):
    """
    This function  takes an integer "disk" and checks if it's movable.
    """
    if len(rod1)!=0 and rod1[-1]==disk:
        return True
    elif len(rod2)!=0 and rod2[-1]==disk:
        return True
    elif len(rod3)!=0 and rod3[-1]==disk:
        return True
    else:
        return False

def getValidMove(ndisks,rod1,rod2,rod3):
    """
    This function repeatedly asks the user for which disk they want to move and
    checks to see if the disk can be legally moved. If it can, it will return
    this disk. Else the function will repeat and ask the user for another disk.
    """
    while True:
        disknum = int(raw_input("Which disk do you want to move?: "))


        if disknum <= ndisks and diskMovable(disknum,rod1,rod2,rod3):
            return disknum
        else:
            print("This disk can't be moved! Try another one. ")

def checkRod(disk,rod):
    """
    This function takes a disk and a list represent a rod and returns True if
    the disk can be placed on that rod. It will also return False, and an error
    message.
    """
    if len(rod) != 0 and disk < rod[-1]:
        return True
    elif len(rod) == 0:
        return True
    else:
        print("I'm sorry, you can't place the disk here!")
        print("Please try again!")
        return False


def getValidRod(disk,rod1,rod2,rod3):
    """
    This function prompts the user for which rod to move the specified disk to.
    The function will also verify that it is possible to move this disk to the
    chosen rod, and if so, it will return the rod number. If not it will repeat
    until the user enters a valid rod for the disk to move to.
    """
    while True:
        user = int(raw_input("Which rod (1 2 or 3) do you want to move to?: "))

        if user == 1:
            rod = rod1
        elif user == 2:
            rod = rod2
        elif user == 3:
            rod = rod3
    
        verify = checkRod(disk,rod)
        if verify == True:
            return rod
        else:
            print("That disk can't be moved to that rod. Try again!")
        
def move(disk,rodnum,rod1,rod2,rod3):
    """
    This function will change the state of the rods to move the disk from its
    current rod to the rod of choice. It runs on the basis that the move has
    already been checked to be legal.
    """
    if len(rod1)!=0 and disk == rod1[-1]:
        rod1.pop()
    elif len(rod2)!=0 and disk == rod2[-1]:
        rod2.pop()
    elif len(rod3)!=0 and  disk == rod3[-1]:
        rod3.pop()
    
    rodnum.append(disk)
    return rodnum

def isGameOver(rod1,rod2,rod3):
    """
    This function returns True if all the disks are on the final rod (for use).
    Returns False and a message if not.
    """
    if len(rod2)==0 and len(rod1)==0:
        return True
    else:
        print("Game is not over!")
        return False

def printState(rod1,rod2,rod3):
    """
    This function prints the current state of the puzzle.
    """
    print(rod1)
    print(rod2)
    print(rod3)
    
main() 
