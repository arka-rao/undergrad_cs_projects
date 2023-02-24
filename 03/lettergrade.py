# lettergrade.py
"""
This is a program that asks the user to enter in a score, and gives back
a letter grade associated with that score. Defined score ranges for each
letter grade are involved in the program.

Written by Arka Rao
February 09, 2016
"""
#inform user of the intent of the program
#ask user to input grade
#write multi way if statements that print letter grade for given score
#if score not in 0-100, inform user that the score is invalid

def main():
    print("")
    print("This program will calculate a letter grade based on your score.")
    print("")
    grade = int(raw_input("What is your score?: "))
    print("")
    if grade <=59 and grade>=0:
        print("You did not pass this test (Grade = NC)")
    elif grade >=60 and grade <=69:
        print("You earned a D.")
    elif grade >=70 and grade <=79:
        print("You earned a C.")
    elif grade >=80 and grade <=89:
        print("You earned a B.")
    elif grade >=90 and grade <=100:
        print("You earned an A.")
    else:
        print("I'm sorry, %d is not a valid score for this test." %(grade))
    print("")

main()
