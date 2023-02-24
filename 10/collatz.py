"""
# solve the collatz problem here

This function takes a number via user input and runs it through a mathematical
function that is part of the Collatz Conjecture. The function collatz() here
takes the user input and prints each number in the sequence as well as returns
the number of steps needed to reach 1.

Written by Arka Rao
April 12, 2016
"""

import exceptions

def main():
    while True:
        try:
            n = int(raw_input("Enter a starting number: "))
            if n < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please enter a valid, positive, nonzero integer")
            
    print(n)
    numSteps = collatz(n)
    print("Number of steps = %4d for n = %d"%(numSteps,n))

def collatz(n):
    if n == 1:
        return 0
    else:
        if n%2 == 0:
            even = n/2
            print(even)
            return(collatz(even)+1)  #recursive way of accumulating
        else:
            odd = 3*n + 1
            print(odd)
            return(collatz(odd)+1)
            
    

main()
