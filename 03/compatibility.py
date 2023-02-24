# compatibility.py
"""
This program asks the user to answer a series of questions about the
things they like, and compares it to a stored set of preferences. Based
on the number of preferences that match, a specific response is generated.

Written by Arka Rao
February 09, 2016
"""
#inform user of the intent of the program
#create lists for preferences and types
#create accumulator variable for ending match statement
#build loop that responds to user input of their preference
#inside loop, develop accumulator variable
#use multiway if statement, incorporating accumulator, to show match

def main():
    print("")
    print("This program will ask you for some things that you like")
    print("and compare it to my preferences. Let's see if they match!")
    print("")
    
    types = ["food", "band", "celeb","drink"]
    mypref = ["tacos", "RHCP", "DJ Khaled", "milkshakes"]
    total = 0

    for i in range(len(types)):
        userpref = raw_input(str(i+1)+". What's your favorite %s? "%(types[i]))
        if userpref == mypref[i]:
            print(">>>>>>>That is my favorite %s too!" %(types[i]))
            total = total + 1
        else:
            print(">>>>>>>%s is okay, but I prefer %s" %(userpref,mypref[i]))

    print("")
    if total == 1:
        print("We have %s out of 4 preferences the same. Not bad!" %(total))
    elif total == 2:
        print("We have %s out of 4 preferences the same. Nice!" %(total))
    elif total == 3:
        print("We have %s out of 4 preferences the same. Alright!!" %(total))
    elif total == 4:
        print("We have %s out of 4 preferences the same. Wow!" %(total))
    else:
        print("We have 0 out of 4 preferences the same. Bummer!")
    print("")
        
main()
