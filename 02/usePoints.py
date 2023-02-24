# CS21 Spring 2016
# usePoints.py
"""
This program helps a user figure out how to use their leftover points at
SciBar at the end of a semester.

Written by Arka Rao
February 5th, 2016
"""
#Print introductory statement
#Ask user for current balance, favorite item, and price of that item
#calculate how many of item they can buy
#calculate how many points they have left after purchase
#print how many they can buy of item and their remaining balance

def main():
    print("")
    print("Welcome to the Science Center Coffee Bar")
    print("----------------------------------------")

    points = float(raw_input("Enter your point balance: $"))
    item = raw_input("Enter your favorite coffee bar item: ")
    price = float(raw_input("Enter price of %s: $" %(item) ))

    canBuy = points/price
    left = points%price

    print("You can buy %d %s and still have $%.2f left." % (canBuy,item,left))
main()
        
