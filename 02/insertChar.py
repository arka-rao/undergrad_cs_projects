# CS21 Spring 2016
# insertChar.py

"""
This is a program that asks the user for some text, a specific character, and
a number of repetitions, and returns that text with the character inserted
repeatedly between each letter.

Written by Arka Rao
February 02, 2016
"""
#ask user for text, characters, repetitions
#accumulate a string where character is inserted repeatedly between letters
#print result

def main():

    print(" ")
    
    text = raw_input("Enter some text: ")
    character = raw_input("Enter character to insert: ")
    repetitions = raw_input("Enter number of repetitions: ")

    print(" ")
    
    chStr = " "
    for i in range(len(text)):
        chStr = chStr + text[i:i+1] + str(character)*int(repetitions)

    print(str(chStr))

    print(" ")
main()
