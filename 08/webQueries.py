"""
This program allows the user to input words and find out how many times they appear on a list
of given websites. It also prints the number of unique words per website.

Written by Arka Rao
April 1st, 2016
"""
from bs4 import BeautifulSoup
from string import *
import urllib2

def main():
    urls = getURLs()
    d = {}

    print("")
    for website in urls:
        uniqueWords = extractWords(website)
        uniqueWordCount = len(uniqueWords)
        print("URL: %s"%(website))
        print("Has %d unique words"%(uniqueWordCount))
        print("")
        d[website] = countWords(uniqueWords)
    
    while True:
        query = raw_input("Enter a query (or q to quit): ")
        if query == "q":
            print("Quit program")
            print("")
            break
        else:
            words = query.split()
            ls = []
            for key in d:
                numWords = 0
                for word in words:
                    value = d.get(key)
                    count = findWordCount(word,value)
                    numWords += count
                urlCountList = [numWords,key]
                if numWords > 0:
                    ls.append(urlCountList)

                    
        ls.sort()
        if len(ls)==0:
            print("No relevance found")
        else:
            for i in range(len(ls)-1,-1,-1):
                wordCount = ls[i][0]
                url = ls[i][1]
                print("Relevance: %s %s" %(wordCount,url))
            
        print("-"*42)
        
def findSortedPosition(word, sortedWordCounts):
    """
    Input: A word as a string and a sorted list of [word, count] pairs.
    Returns: An integer representing the index location of the given word
    in the sorted list.  If the given word is not in the list, then inserts 
    a new sublist [word, 0] at that location.
    Purpose: Uses a linear search to find the index of where the word
    appears (or should appear) in the given list.
    """
    for i in range(len(sortedWordCounts)):
        if word == sortedWordCounts[i][0]:
            return i
        elif word < sortedWordCounts[i][0]:
            sortedWordCounts.insert((i),[word,0])
            return i
            
    sortedWordCounts.append([word,0])
    return len(sortedWordCounts)-1

def countWords(wordList):
    """
    Input: A list of words that may contain repeated words.
    Returns: A sorted list of [uniqueWord, count] sublists based on the 
    given wordList created by repeated linear searches.
    Purpose: Uses findSortedPosition to build the word count list.
    """

    sortedWordsWithCounts = []
    for word in wordList:
        position = findSortedPosition(word,sortedWordsWithCounts)
        sortedWordsWithCounts[position][1] += 1
    return sortedWordsWithCounts

def findWordCount(word, sortedWordCounts):
    """
    Input: A word as a string and a sorted list of [word, count] sublists.
    Returns: An integer representing the count associated with the word.
    If the word is NOT in the list returns 0.
    Purpose: Uses a binary search to find the word in the given list and
    return it's count.
    """
    low = 0
    high = len(sortedWordCounts)-1
    while low <= high:
        mid = (low+high)/2
        if sortedWordCounts[mid][0]==word:
            position = mid
            count = sortedWordCounts[position][1]
            return count
        elif word < sortedWordCounts[mid][0]:
            high = mid-1
        else:
            low = mid+1
    return 0
        
def unitTests1():
    test1 = [["apple", 2], ["banana", 1]]
    test2 = [["apple", 2], ["mango", 5]]
    assert findSortedPosition("apple", []) == 0
    assert findSortedPosition("apple", test1) == 0
    assert findSortedPosition("mango", test1) == 2
    assert findSortedPosition("banana", test2) == 1

def unitTests2():
    list1 = ["apple", "banana", "apple", "mango", "apple", "mango"]
    counts = countWords(list1)
    assert counts == [["apple", 3], ["banana", 1], ["mango", 2]]

def unitTests3():
    list1 = ["apple", "banana", "apple", "mango", "apple", "mango"]
    counts = countWords(list1)
    assert findWordCount("banana", counts) == 1
    assert findWordCount("mango", counts) == 2
    assert findWordCount("cherry", counts) == 0
    assert findWordCount("plums", counts) == 0

def getURLs():
    """
    Inputs: None
    Returns: A list of valid URLs for users in the CS department we would
    like to include in our search engine.
    """
    users = ["adanner", "brody", "bryce", "knerr", "kwebb",  "meeden", 
             "newhall", "richardw", "sindhu", "soni", "zpalmer"]
    swatCS = "http://www.cs.swarthmore.edu"
    urls = []
    for user in users:
        urls.append(swatCS+"/~"+user)
    return urls

def extractWords(url):
    """
    Input: A url as a string
    Returns: A list of all words, in the order that they appear, on the web 
    page associated with the given url. It excludes words shorter than 3 
    characters and numeric data.  Will include strings that contain a mix
    of letters and numbers like 'cs21'. 
    """
    src = urllib2.urlopen(url)   #open the file associated with the URL
    soup = BeautifulSoup(src)  
    textString = soup.get_text() #parse the web page to remove the text
    words = textString.split()   #split the text into individual words
    relevantWords = []           
    for word in words:
        try:
            word = lower(str(word)).strip('.,()!:;?')
        except UnicodeEncodeError:
             #ignore Unicode words
             continue
        if len(word) < 3 or word.isdigit():
            #ignore short words and anything that is all digits
            continue
        relevantWords.append(word)
    return relevantWords


if __name__ == '__main__':
    main()
