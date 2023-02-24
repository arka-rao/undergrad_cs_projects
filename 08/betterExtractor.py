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
            # ignore Unicode words
            continue
        if len(word) < 3 or word.isdigit():
            # ignore short words and anything that is all digits
            continue
        relevantWords.append(word)
    return relevantWords
