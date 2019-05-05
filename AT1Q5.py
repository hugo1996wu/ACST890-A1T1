
#Question 5
#Saved as AT1Q5.py
#load module datetime
from datetime import *
import sys
#Make 1st and 2nd command argument as month and date input
#Also assign them as variable m and d respectively
m=int(sys.argv[1])
d=int(sys.argv[2])
#Change all input type as date
datet=date(2016,m,d)
date1=date(2016,3,20)
date2=date(2016,6,20)
#Check required condition
if date1<datet<date2:
    print("True")
else :
    print("False")