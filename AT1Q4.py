#Question 4
#Saved as AT1Q4.py
#Load module random as rd, also load module sys
import random as rd
import sys
#Make 1st and 2nd command argument as 1st and 2nd integer input
#Also assign them as variable a and b respectively
a=int(sys.argv[1])
b=int(sys.argv[2])
#Check required condition (b>a)
if b>a:
    cond=True
else :
    cond=False
#Ask user to input a greater no for b until the condition is met
while not cond:
    b=int(input('Please enter a greater value for the second number:'))
    if b>a:
        cond=True
    else :
        cond=False
#Print out the required result
print(rd.randint(a,b))
