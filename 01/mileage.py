"""
This is a program that asks the user for their current running mileage, and
then displays a 16-week program that increases their mileage by 10% per week.

Written by Arka Rao
January 26th, 2016
"""
#Inform user of the intent of the program
#Ask them for their current mileage
#Convert variable to a float
#Create a loop that also repeatedly overwrites the variable to get the schedule


print(" ")
print("This program will help you develop a 16 week running program to")
print("optimize your gains during your running workouts.")
print("Please enter your current weekly mileage.")
print(" ")


currentMileage = raw_input("Current Weekly Mileage: ")
print(" ")


currentMileage = float(currentMileage)


print("To optimize your gains over the next 16 weeks, follow this training")
print("schedule.")
print(" ")
for i in range(1,17,1):
    currentMileage += currentMileage * 0.1
    print("Week" + " " + str(i) + ":" + " " + str(currentMileage))
print(" ")
    
    







    
