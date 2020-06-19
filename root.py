# some algorithms for root finding
import numpy as np

# bisection method
#
# input: function f, xa and xb such that a root lies between them and an error tolerance tol
#
# output: approximate solution xc
#
# example setup/call:
#def f(x):
#    return x**3 + x - 1
#
#print(bisect(f,0,1,0.00005))
# >> 0.682342529296875

def bisect(f,xa,xb,tol):
    if(f(xa)*f(xb)>=0):
        print("Error, root not bracketed correctly!")
    else:
        fa = f(xa)
        fb = f(xb)
        while((xb-xa)/2>tol):
            xc = (xa+xb)/2
            fc = f(xc)
            if fc==0:
                return xc
            else:
                if fa*fc<0:
                    xb = xc
                    fb = fc
                else:
                    xa = xc
                    fa = fc
        return (xa+xb)/2