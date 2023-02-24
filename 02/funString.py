# CS21 Spring 2016
# funString.py

"""
This is a program that creates a fun design out of a user-entered string.

Written by Arka Rao
February 02,2016
"""

def main():
    text = raw_input("Enter some text: ")

    print("")
    
    funtext = " "
    for i in range(len(text)):
        funtext = text[0:int(len(text)-i)]
        print(str(funtext))

    reversefuntext = " "
    for i in range(len(text)):
        reversefuntext = text[0:i+1]
        print(str(reversefuntext))

    print("")
                              
main()
