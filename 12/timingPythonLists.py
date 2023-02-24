"""
Use timing tests to confirm that python is using consecutive memory to
store its lists.
"""

from time import time

def main():
    size = 100
    trials = 10
    print("\ntesting indexing on PYTHON lists")
    for i in range(8):
        avgIndexing(size, trials)
        size *= 2

    print("\ntesting inserting on PYTHON lists")
    size = 100
    trials = 10
    for i in range(8):
        avgInserting(size, trials)
        size *= 2

def timeIndexing(n):
    """
    Inputs: n, size of a list to test
    Returns: average time per indexing operation
    Purpose: Time indexing on python lists. If python lists are stored
    in consecutive memory then indexing should occur in constant time
    regardless of the size of the list.
    """
    ls = range(n)
    start = time()
    for i in range(10000):
        x = ls[n/2]
    end = time()
    return end-start

def avgIndexing(n, trials):
    """
    Inputs: n, size of list to test, trials number of tests to run
    Returns: None, prints results of tests
    """
    total = 0.0
    for i in range(trials):
        total += timeIndexing(n)
    print("For list of size: %8d append time: [%.10f]" % (n, total/trials))

def timeInserting(n):
    """
    Inputs: n, size of a list to test
    Returns: average time for inserting at the front of a list
    Purpose: Time insertion on python lists. If python lists are stored
    in consecutive memory then insertion should get increasingly slower
    as the size of the list increases.  
    """
    ls = range(n)
    start = time()
    for i in range(1000):
        ls.insert(0, 22)
    end = time()
    return end-start

def avgInserting(n, trials):
    """
    Inputs: n, size of list to test, trials number of tests to run
    Returns: None, prints results of tests
    """
    total = 0.0
    for i in range(trials):
        total += timeInserting(n)
    print("For list of size: %8d insert time: [%.10f]" % (n, total/trials))

 
main()
