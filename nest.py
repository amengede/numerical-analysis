# nested multiplication for polynomial evaluation (Horner's method)
#
# input: degree d of polynomial, array of (d+1) coefficients c in ascending order of power, x coefficient to evaluate at,
# and array of d base points b if needed
#
# output: value y of polynomial at x

import numpy as np

def nest(d,c,x,b=-1):
    if b==-1:
        b = np.zeros((d))
    y = c[d]
    for i in range(d-1,-1,-1):
        y = y*(x-b[i]) + c[i]
    return y

#example call, should evaluate to 1.25
#d = 4
#c = np.array([-1, 5, -3, 3, 2])
#x = 0.5

#print(nest(d,c,x))