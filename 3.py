#Normal Distribution
import scipy.stats as stats

mean=float(input("Enter the mean:"))
std=float(input("Enter the standard devaiation:"))
lower_lim=float(input("Enter the lower limit of normal variate:"))
upper_lim=float(input("Enter the upper limit of normal variate:"))

cdf_upperlim=stats.norm.cdf(upper_lim,loc=mean,scale=std) 
cdf_lowerlim=stats.norm.cdf(lower_lim,loc=mean,scale=std)  
prob=cdf_upperlim - cdf_lowerlim 
z_upper=(upper_lim-mean)/std
z_lower=(lower_lim-mean)/std
print("z lower limit: ",z_lower)
print("z upper limit: ",z_upper)
print("Normal probability value: ",prob)