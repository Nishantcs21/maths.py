import numpy as np 
from scipy.integrate import quad

mean= int(input("Enter the mean:"))

lower_lim=int(input("Enter the lower limit (Enter 0 if -infinity):"))
upper_lim=int(input("Enter the upper limit (Enter 0 if infinity):"))

def f(x,mean):
    return (1/mean)* np.exp(-(1/mean)*x)
    

if (lower_lim==0 and upper_lim==0):
    print("The exponential probability value is 1.")

elif lower_lim<=0: # lower limit -infinity
    expo_pdf=quad(f,0,upper_lim, args=(mean))  # For any exponential distribution, negative number to y is same as 0 to y
    print("The exponential probability value is:", expo_pdf)

else:
    expo_pdf=quad(f,lower_lim, upper_lim, args=(mean)) # from lower to upper limit
    print("The exponential probability value is:", expo_pdf)