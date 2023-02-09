import math
 
def f(x, lam):
    return (math.exp(-lam) * lam**x)/(math.factorial(x))

lam=float(input("Enter the mean:"))
p=int(input("Enter the poisson variate:"))

poisson=f(p,lam)
print("The poisson distribution is:", poisson)