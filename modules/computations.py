from inputParams import parameters 
from math import sqrt, pow, sin, cos, atan
import numpy as np

Jt, jerk_eq, Jf, Q, g, a0, v0, y0, xmax, tmax, h, dt, rounding_decimals = parameters.values()

# right-hand side of the autonomous differential equation
def Uprime(u, y):
    try:
        if jerk_eq == "tangential":
            factor1 = Jf * (1 + pow(u, 2)) / (2 * pow(speed(u, y), 2))
            radicand = pow(g/Q, 2) - (Jf * 4 * speed(u, y) * Jt * (1 + pow(u, 2)))
            factor2 = (-1 * g/Q) + sqrt(radicand)
            return factor1 * factor2
        elif jerk_eq == "scalar":
            factor1=-Jt*Q/(g*speed(u,y))
            factor2=(1+pow(u, 2))**2
            return factor1 * factor2
        else:
            exit("JERK_EQUATION must be either 'scalar' or 'tangential'.")
    except OverflowError:
        exit(f"Math Overflow error: the curve is becoming infinitely steep, breaking down some equations."
            f"Try using a shorter curve by decreasing xmax in inputParams.py")

# speed as a function of y
def speed(u, y):
    second_term = 2 * g * (y0 - (y +(u*h))) / Q
    return sqrt(pow(v0, 2) + second_term)


def parabolic_free_fall(divPoint, u, speed, duration):
    t = np.linspace(0, duration, int(duration / dt))
    X = list(range(len(t)))
    Y = list(range(len(t)))
    for i, t in enumerate(t):
        X[i] = divPoint[0] + (abs(speed) * cos(local_angle(u))) * t
        Y[i] = divPoint[1] + (abs(speed) * sin(local_angle(u))) * t - (g/2) * pow(t, 2)
    return X, Y

# this function searches for u and y in U_origins and Y_origins and calculates Uprime at the (i+1)-th and (i-1)-th positions
def Udoubleprime(U_origins, Y_origins, X_origins, u, y):
    U_olength = len(U_origins)
    for i, u_value in enumerate(U_origins):
        if u_value == u:
            if i != 0 and i != U_olength - 1:
                uprime_before = Uprime(U_origins[i - 1], Y_origins[i - 1])
                uprime_after = Uprime(U_origins[i + 1], Y_origins[i + 1])
                hodo_stepsize = X_origins[i + 1] - X_origins[i - 1]
            elif i == 0:
                uprime_before = Uprime(U_origins[i], y)
                uprime_after = Uprime(U_origins[i + 1], Y_origins[i + 1])
                hodo_stepsize = X_origins[i + 1] - X_origins[i]
            elif i == U_olength - 1:
                uprime_before = Uprime(U_origins[i - 1], Y_origins[i - 1])
                uprime_after = Uprime(U_origins[i], y)
                hodo_stepsize = X_origins[i] - X_origins[i - 1]
            slope = (uprime_after - uprime_before) / hodo_stepsize
    return slope


def local_angle(u):
    return atan(u)