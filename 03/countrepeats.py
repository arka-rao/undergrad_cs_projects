# countrepeats.py
"""
This program allows the user to enter some text, and subsequently counts
the number of repeated characters in that text.

Written by Arka Rao
February 9th, 2016
"""
#inform user of program intent
#store user's entered text in variable
#develop accumulator variable
#write forloop that walks through characters in text and overwrites accum.
#print statement with number of repeats
def main():
    print("")
    print("This program lets you enter text and counts the number of repeats")
    print("in that text.")
    print("")
    text = raw_input("Enter some text: ")
    counter = 0
    for i in range(len(text)-1):
        if text[i]==text[i+1]:
            counter = counter + 1
        else:
            counter = counter + 0
    print("There are %d repeats in that string."%(counter))
    print("")
main()
