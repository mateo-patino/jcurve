from inputParams import parameters
from math import pow, sqrt
from sys import exit
import numpy as np


Jt, jerk_eq, Jf, Q, g, a0, v0, y0, xmax, tmax, h, dt, decs = parameters.values()

# declare time, X and Y arrays
X = []
Y = []
if dt != 0:
    t = np.linspace(0, tmax, int(tmax / dt))
else: exit("'dt' cannot equal zero.")

# append x0 and y0
X.append(0) 
Y.append(y0)

def simulated_main():
    
    # calculate X and Y values
    for i in range(1, len(t)):
        newX, newY = newPoint(i, t[i-1])
        X.append(newX)
        Y.append(newY)
    
    # return complete kinematic X and Y arrays 
    return X, Y


# t-notation is used because y'(x) can be written in terms of time with kinematic equations
def yprime(t):
    numerator = -1 * (accel(t)/g)
    denominator = sqrt(1 - pow(accel(t)/g, 2))
    return numerator/denominator


def accel(t):
    return a0 + (Jt * t)


def veloc(t):
    return v0 + (a0*t) + (0.5 * Jt * pow(t, 2))


def newPoint(i, t):
    numerator = veloc(t) * dt
    denominator = sqrt(1 + pow(yprime(t), 2))

    # compute new X and Y values
    newX = X[i-1] + (numerator / denominator)
    newY = Y[i-1] + (yprime(t) * (numerator / denominator))
    return newX, newY

