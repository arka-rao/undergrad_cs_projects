"""
# solve the insideout problem here

This program takes a word that the user enters and turns it inside out,
employing a recursive function to do so.

Written by Arka Rao
4/2/16
"""
import exceptions

def main():
    while True:
        try:
            S = raw_input("Enter a word: ")
            if not S.isalpha():
                raise ValueError
            else:
                break
        except ValueError:
            print("Please enter a valid string.")


    newS =insideOut(S)
    print(newS)

def insideOut(S):
    """
    This function takes a string and uses recursion to turn it inside out, and
    then it returns a new, built up, insideout string.
    """
    if S == "":
        return S
    else:
        low = 0
        high = len(S)-1
        middle = (low+high+1)/2 #adding one accounts for results of the sample runs
        newString = S[0:middle] + S[middle+1:]
        return S[middle] + insideOut(newString)
        
        


main()
