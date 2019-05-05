#Question 3
#Saved as AT1Q3.py
#Load module sys
import sys
#Make first command argument in integer type, and assign it as varaible a
a=int(sys.argv[1])
#Check if it is leap year by divisibility condition
#The algorithm can be found from wikipedia -
#https://en.wikipedia.org/wiki/Leap_year#Algorithm
if a%4!=0:
    print('This is not leap year')
elif a%100!=0:
    print('This is a leap year')
elif a%400!=0:
    print('This is not leap year')
else :
    print('This is a leap year')
