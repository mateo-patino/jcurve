from inputParams import parameters
from math import pow, sqrt, isnan
from sys import exit, argv
from modules.computations import Uprime
import numpy as np


Jt, Jf, Q, g, a0, v0, y0, xmax, tmax, h, dt, decs = parameters.values()

# declare array for U_i, Y_i, and X_i values
U = []
Y = []
X = np.linspace(0, xmax, int(xmax / h)).tolist()

# append initial height
Y.append(y0)

# calculate U0 (y'(x) at t = 0) and append to U array
try:
    U0 = -1 * (a0/g) / sqrt(1 - pow(a0/g, 2))
except (ValueError, ZeroDivisionError):
    exit(f"An error occurred calculating the initial value of U-prime. INITIAL_ACCELERATION cannot "
         "be greater than or equal to GRAVITATIONAL_ACCELERATION. Try a smaller value for the object's initial acceleration. ")
U.append(U0)


def rungekutta_main():

    global X, Y, U
    # calculate new U and Y values and record them in lists
    break_point = len(X)
    for i in range(1, len(X)):
        k1, k2, k3, k4 = rungekutta_kvalues(U[i-1], Y[i-1])
        new_U = U[i-1] + (h/6)*(k1 + (2*k2) + (2*k3) + k4)
        if not isnan(new_U): U.append(new_U)
        else: 
            break_point = i
            break
        new_Y = Y[i-1] + (U[i-1] * h)
        if not isnan(new_Y): Y.append(new_Y)
        else: 
            break_point = i
            break

    # Remove X values that correspond to non-defined values of U or Y to ensure same dimensions
    if break_point < len(X):
        X = X[:break_point]
        Y = Y[:break_point]
        U = U[:break_point]
    
    # Return complete X, Y, and U arrays
    return np.array(X), np.array(Y), np.array(U)


def rungekutta_kvalues(u, y_i):
    k1 = Uprime(u, y_i)
    k2 = Uprime(u + (h * (k1/2)), y_i)
    k3 = Uprime(u + (h * (k2/2)), y_i)
    k4 = Uprime(u + (h * k3), y_i)
    return k1, k2, k3, k4
