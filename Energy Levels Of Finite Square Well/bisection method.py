# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:28:45 2019

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

                                ##givenvalues
a = 0.05         #nm
v0 = 40         #eV
mc_sq = 0.511e6
hc = 197.3
K = (2*mc_sq)/((hc)**2)

    
                                ##Defining the eqution to be solved (eqn 5.1)    
def f(x):
     l = np.sqrt(K*(v0-x))
     k = np.sqrt(K*x)
     return l * np.tan(l*a) -k 


                                ##creating epsilon space 
e_s = np.linspace(25,27,50)

plt.plot(e_s, f(e_s))
for i, e in enumerate(f(e_s)):
    print(e_s[i],e)
plt.plot(e_s, 0*e_s)
plt.show()


                                ##Bisect function
def bisection(a,b,tol):
    xl = a                      ##left value
    xr = b                      ##right value
                                ##check if root (midpoint) lies within interval [a,b]
    while (np.abs(xl-xr)>= tol):            
        c = (xl +xr)/2
        prod = f(xl)*f(c)
        if prod > tol:
            xl = c
        else:
            if prod < tol:
                xr =c
    return c

answer = bisection(25.5,27.5, 1e-10)
print("The value for epsilon is ",answer)