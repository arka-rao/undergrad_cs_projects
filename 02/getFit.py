# CS21 Spring 2016
# getFit.py

"""
This program helps users track the number of steps they walk per day. It does
this by requesting the user's weekly goal, and then asks for the daily total
over the course of a week. Each day, it will display the current total, steps
needed to achieve the goal, and the average number of steps per day.

Written by Arka Rao
February 5th, 2016
"""

def main():
    print(" ")
    goal = int(raw_input("Enter your weekly step goal: "))
    print(" ")
    sofar = 0
    for i in range(1,8):
        daysteps = int(raw_input("Day %s Steps: "%(i)))
        sofar = sofar + daysteps
        rem = goal - sofar
        avg = sofar/float(i)
        print("Steps so far: %d Steps remaining: %d Avg per day: %.1f"\
              %(sofar, rem, avg))
    print(" ")
main()
        
