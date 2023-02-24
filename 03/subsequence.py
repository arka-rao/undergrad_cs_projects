# subsequence.py
"""
This program asks the user to enter some text and a pattern string, and then
looks to see if the pattern string is a "subsequence" of the text string.

Written by Arka Rao
February 11th, 2016
"""
#ask user to enter text and pattern
#set up accumulator variable
#build forloop that walks through text and checks if char matches with pattern
#once n == len(pattern), stop loop
#else, n = n + 0
#once n == len(pattern), print that pattern is a subsequence of text
#if not the cast, print that pattern isn't a subsequence of text
def main():
    text = raw_input("What is the text string? ")
    pattern =raw_input("What is the pattern string? ")
    n = 0

    for i in range(len(text)-1):
        if text[i] == pattern[n]:
            n = n + 1
            if n == len(pattern):
                break
        else:
            n = n + 0

    if n == len(pattern):
        print("[%s] is a subsequence of [%s]"%(pattern,text))
    else:
        print("[%s] is not a subsequence of [%s]"%(pattern,text))
main()        
