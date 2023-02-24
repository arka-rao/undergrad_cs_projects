"""
contributions.py

This is a program that handles all of the donation information for the current
2016 election frontrunners. It allows the user to peruse the donation sorted by
zipcode, city, or state. When sorted by state, it displays a map of donations by
zipcode, plotted as either red or blue dots.

Written by Arka Rao
April 8th, 2016
"""

"""
#Task List Lab09
#try and except in zipquery           #done
#try and except in cityquery          #done
#fix repeats in cityquery             #done
#try and except in statequery         #done
#fix bug in forloop in zipquery       #done
#descending order in zipquery         #done
#statequery                           #done
#graphics                             #done
#import large file                    #done
"""


#from boundaries import *
from math import sqrt
import exceptions

def main():
  # TO DO: implement the main program!
  #print("in main")
  #testSort()

  campaignContributions=getContributions("/usr/local/doc/contributions2016.txt")
  entryNumber = len(campaignContributions)
  d = getLatLong("/usr/local/doc/zipcodes.txt")
  
  print("")
  print("In this program, you can search for campaign contribution")
  print("information by zip code, city, or state.")
  print("")
  print("There are a total of %d contribution entries."%(entryNumber))
  print("")
  print("Please choose from the following options")
  print("(1) search by zip code")
  print("(2) search by city")
  print("(3) search by state")
  print("(4) quit the program")

  while True:
    query = validQuery()
    if query == 4:
      print("Okay, see you later!")
      break
    elif query == 1:
      zipQuery(campaignContributions)
    elif query == 2:
      cityQuery(campaignContributions)
    elif query == 3:
      stateQuery(campaignContributions,d)
    else:
      print("Please enter a valid option")
      
        

def listSort(L, index):
  """
  Inputs: 
    -- L, a list of lists, to be sorted
    -- index, an integer representing what to sort on
  Returns: Nothing, but L becomes sorted
  Purpose: Sort a list-of-lists by a particular index.

  Example:  
  listSort([["apple",4], ["pear", 1], ["banana", 3], ["mango", 2]], 0)  
  should updates the list to be
  [["apple",4], ["banana", 3], ["mango", 2], ["pear", 1]]
  """
  print("In list sort beginning, this is L: %s"%(L))
  for i in range(len(L)):
    iSmallest = i
    for j in range(i+1,len(L)):
      if L[j][index] < L[iSmallest][index]:
        iSmallest = j
    L[i],L[iSmallest]=L[iSmallest],L[i]
  print("At end of list sort, this is L: %s"%(L))
        

  
def stateQuery(contributions, zips):
  """
  Inputs:  
    contributions: a lsit of contribution data by zipcode and campaigner
    zips:  a dictionary of zipcode/[lat/long] pairs
  Returns:
    None
  Purpose:  implement entire run of user asking for contribution information 
    by state.
  """
  
  unitedStates = ["AL","AK","AS","AZ","AR","CA","CO","CT","DE","DC","FM","FL","GA","GU","HI","ID","IL","IN","IA","KS","KY","LA","ME","MH","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","MP","OH","OK","OR","PW","PA","PR","RI","SC","SD","TN","TX","UT","VT","VI","VA","WA","WY","WV","WI","WY"]
  #taken from pe.usps.gov/text/pub28/28apb.htm
  while True:
    try:
      stateCode = raw_input("Enter a two letter state code: ")
      if not stateCode.isalpha():
        raise ValueError
      elif len(stateCode) < 2 or len(stateCode) > 2:
        print("The state code must be two letters in length.")
      elif stateCode.upper() not in unitedStates:
        print("That isn't a valid state.")
      else:
        break
    except ValueError:
      print("Please enter a valid state code.")
  print("")
  
  
  stateCode = stateCode.upper()
  stateList = []
  for contribution in contributions:
    if contribution[2] == stateCode:
      stateList.append(contribution)

  #now we have list of lists with only the state entered

  clintonList = []
  cruzList = []
  kasichList = []
  sandersList = []
  trumpList = []
  
  for contribution in stateList:
    if contribution[3] == "Clinton":
      clintonList.append(contribution)
    elif contribution[3] == "Cruz":
      cruzList.append(contribution)
    elif contribution[3] == "Kasich":
      kasichList.append(contribution)
    elif contribution[3] == "Sanders":
      sandersList.append(contribution)
    elif contribution[3] == "Trump":
      trumpList.append(contribution)

  #no contributions check
  if len(clintonList) == len(cruzList) == len(kasichList) == len(sandersList) == len(trumpList) == 0:
    print("There were no contributions for that state.")
    print("")
    return
    
  
  candidates = [clintonList,cruzList,kasichList,sandersList,trumpList]
  candidateNames = ["Clinton","Cruz","Kasich","Sanders","Trump"]
  #now we have list of lists sorted by candidate sorted by state

  for candidateList in candidates:
    sortList(candidateList,6)
    candidateList.reverse()
  
  for i in range(len(candidateNames)):
    if candidates[i] != []:
      print("Top five contribution zip codes for %s in %s:" %(candidateNames[i],stateCode))
    if len(candidates[i]) < 5:
      for contributions in candidates[i]:
        zipCode = contributions[0]
        city = contributions[1]
        state = contributions[2]
        number = contributions[5]
        donations = contributions[6]
        print("%s, %s %s: %d contributions totalling $%d"%(state,city,zipCode,number,donations))
    else:
      for j in range(5):
        zipCode = candidates[i][j][0]
        city = candidates[i][j][1]
        state = candidates[i][j][2]
        number = candidates[i][j][5]
        donations = candidates[i][j][6]
        print("%s, %s %s: %d contributions totalling $%d"%(state,city,zipCode,number,donations))
    print("")

            
  print("****Click anywhere on the graphics window to continue.****")
  
  statewin = getStateGraphWin(stateCode)
  
  if statewin != None:
    demoDonations = 0
    repubDonations = 0
    zipCodeCheck = stateList[0][0]
    for i in range(len(stateList)):
      if stateList[i][3] == "Cruz" or stateList[i][3] == "Kasich" or stateList[i][3] == "Trump":
        repubDonations += stateList[i][6]
      else:
        demoDonations += stateList[i][6]
      X = zips[zipCodeCheck][1]
      Y = zips[zipCodeCheck][0]
      zipCodeCheck = stateList[i][0]
      if repubDonations > demoDonations:
        point = Point(X,Y)
        point.setFill("red")
        point.draw(statewin)
      else:
        point = Point(X,Y)
        point.setFill("blue")
        point.draw(statewin)
      
    statewin.getMouse()
    statewin.close()
    
    
def cityQuery(contributions):
  """
  Inputs:  
    contributions: a lsit of contribution data by zipcode and campaigner
  Returns:
    None
  Purpose:  implement entire run of user asking for contribution information 
    by city.
  """
  print("")
  print("searching by city...")

  print("")
  while True:
    try:
      city = raw_input("Enter a city: ")
      if not city.isalpha():
        raise ValueError
      else:
        break
    except ValueError:
      print("Please enter a valid city")

  cityUpper = city.upper()
  cityContributionLS = []
  for contribution in contributions:
    if contribution[1][0:len(cityUpper)] == cityUpper:
      cityContributionLS.append(contribution)

  if len(cityContributionLS) == 0:
    print("No entries found for that city.")
    print("")
    return
    
  print("")
  print("Here are all the cities I can find that start")
  print("with %s and have contributions..."%(cityUpper))
  print("")

  demo = 0
  repub = 0
  demoCandidateLS = ["Clinton","Sanders"]
  repubCandidateLS = ["Cruz","Kasich","Trump"]

  if cityContributionLS[0][3] in demoCandidateLS:
    demo = cityContributionLS[0][6]
    repub = 0
  else:
    repub = cityContributionLS[0][6]
    demo = 0
    
  if len(cityContributionLS) == 1:
    city = cityContributionLS[0][1]
    zipCode = cityContributionLS[0][0]
    state = cityContributionLS[0][2]
    print("%s, %s, %s, Democrat: $%d, Republican: $%d"%(city.upper(),state,zipCode,demo,repub))
    
  for i in range(1,len(cityContributionLS)):
    city = cityContributionLS[i][1]
    zipCode = cityContributionLS[i][0]
    state = cityContributionLS[i][2]
    if zipCode != cityContributionLS[i-1][0]:
      print("%s, %s, %s, Democrat: $%d, Republican: $%d"%(city.upper(),state,zipCode,demo,repub))
      if cityContributionLS[i][3] in demoCandidateLS:
        demo = cityContributionLS[i][6]
        repub = 0
      else:
        repub = cityContributionLS[i][6]
        demo = 0 
    else:
      if cityContributionLS[i][3] in demoCandidateLS:
        demo += cityContributionLS[i][6]
      else:
        repub += cityContributionLS[i][6]
      
  print("")
    
      
  
def zipQuery(contributions):
  """
  Inputs:  
    contributions: a lsit of contribution data by zipcode and campaigner
  Returns:
    None
  Purpose:  implement entire run of user asking for contribution information 
    by city.
  """
  print("")
  while True:
    try:
      userZip = int(raw_input("Enter a 5-digit ZIP code: "))
      if len(str(userZip)) < 5:
        raise ValueError
      else:
        break
    except ValueError:
      print("Please enter a valid ZIP")

  userZip = str(userZip)

  zipCheck = 0
  
  for contribution in contributions:
    if userZip == contribution[0]:
      city = contribution[1]
      state = contribution[2] 
      print("") 
      zipCheck += 1
      
      
  if zipCheck ==0:
    print("")
    print("No contribituion information found for %s"%(userZip))
    return

  print("Contribution information for "+ city + ", " + state + " " + userZip)
  #weird error where print formatting broke the program, this way works 4/8/16

  zipList = [] 
  for contribution in contributions:
    if userZip in contribution:
      zipList.append(contribution)

  sortList(zipList,6)
  zipList.reverse()

  for i in zipList:
    print("%s: %d contributions totalling $%d"%(i[3],i[5],i[6]))

  print("")
  
def getContributions(fileName):
  """
  Inputs:  fileName, the name of the file containing the campaign contribution
    database.
  Returns: a list of campaign entries.
  Purpose: load campaign information from file into list.
OA  """
  inFile = open(fileName, "r")
  entries = []
  for line in inFile:
    line = line.strip()
    entry = line.split(",")
    entry[5] = int(entry[5])
    entry[6] = int(entry[6])
    entries.append(entry)
  inFile.close()
  return entries

def getLatLong(fileName):
  """
  Inputs: the name of the file containing the zip code lat/long data
  Returns: a dictionary containing lat/long data.  
  Purpose:  Load geographic information about zip codes from a file into 
    a dictionary.
    Keys in the dictionary are 5-digit zip code strings.
    Values in the dictionary are [lat,long] float lists.
  For example, the zip code for Swarthmore is 19081.
  The latitiude is 39.897562 degrees North, -075.346584 degrees East 
  (i.e., 75.346584 degrees west)
  In the dictionary, the key is "19081", the value [39.897562,-075.346584]
  """
  inFile = open(fileName, "r")
  D = {}                        # create new dict
  for line in inFile:
    line = line.strip()
    zipline = line.split(",")
    D[zipline[0]] = [float(zipline[1]),float(zipline[2])]
  return D

def testSort():
  """
  Inputs: None
  Returns: None
  Purpose: unit tests for sorting function
  """
  L = [["apple",4], ["pear", 1], ["banana", 3], ["mango", 2]]
  print("In test sort")
  print(L)
  listSort(L,0)
  assert(L==[["apple",4], ["banana", 3], ["mango", 2], ["pear", 1]])
  print("In test sort")
  print(L)
  listSort(L,1)
  assert(L==[["pear", 1], ["mango", 2], ["banana", 3], ["apple",4]])
  print("In test sort")
  print(L)
  L = []
  assert(L==[])
  print("In test sort")
  print(L)
  L = [["apple",4]]
  assert(L==[["apple",4]])
  print("listSort tests passed!")

def validQuery():
  while True:
    try:
      query=int(raw_input("Enter an option from the list: "))
    except ValueError:
      print("Please enter a valid number from 1 to 4.")
      continue
      
    if query == 1 or query == 2 or query == 3 or query == 4:
      return query
    else:
      print("Please enter an option from the list.")

def sortList(candidateList,index):
  """
  This function takes a list of lists and sorts by a value in each list within the list of lists. It returns the sorted list.
  It uses bubble sort.
  """

  while True:
    nswaps = 0
    for i in range(len(candidateList)-1):
      if candidateList[i][index] > candidateList[i+1][index]:
        candidateList[i],candidateList[i+1] = candidateList[i+1],candidateList[i]
        nswaps += 1
    if nswaps == 0:
      break
  
      
main()
