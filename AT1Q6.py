#Question 6
#Saved as AT1Q6.py
#Load module math
import math as mt
#Ask user to input principal, interest rate and time
#Assign them to variables with correct type
P=float(input('Input invested amount:'))
r=float(input('Input interest rate (continuously compounded):'))
t=float(input('Input the number of years:'))
#Print desired value
print(P*mt.e**(r*t))
