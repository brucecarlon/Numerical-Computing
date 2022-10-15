# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:38:38 2019

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy import optimize  
                                    ##Defining secant method form
def secant(fn,x1,x2,tol,maxiter):
    for iteration in range (maxinter):
        xnew = x2 -(x2-x1)/(fn(x2) - fn(x1)) * fn(x2)
        if abs(xnew - x2) < tol : break
        else:
            x1 = x2
            x2 = xnew
        
    else:
        print("max iter reached")
    return xnew, iteration

                                    ##Given value
a = 0.05         #nm
v0 = 40         #eV
mc_sq = 0.511e6
hc = 197.3
K = (2*mc_sq)/((hc)**2)

def fn(x):
     l = np.sqrt(K*(v0-x))
     k = np.sqrt(K*x)
     return l * np.tan(l*a) -k
 
                                    ## left and right end points for the root search    
x1 = 25
x2 = 28
maxinter = 100
r,n = secant(fn,x1,x2,0.000001,100)
print("The value for epsilon is", r, "after", n ,"iterations")