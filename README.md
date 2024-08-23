# Modelling a Constant-Jerk Curve 🎢
This repository contains code for the paper "**Jerk, Speed, and Acceleration Inclined Surfaces**." The Python scripts here implement a tool to visualize the constant-jerk _y=y(x)_ curve presented in the paper. A hodograph of the jerk and acceleration vectors for an object traveling along the curve is also available.

## Installation
Our code requires [Python3](https://www.python.org/downloads/) and certain external libraries ("dependencies") to run. First, make sure you have Python3 installed in your system. Then, install our code's dependencies by running 
```
pip install -r requirements.txt
```
If you encounter issues with the command above, you can install each dependency separately using 
```
pip install dependency_name==version_number
```
The version number for each dependency can be found in the `requirements.txt` file. 

## Usage
As a user, there are two ways to interact with our code: by running `curves.py` or `hodograph.py`. Running `curves.py` will allow you to visualize two curves – the curve yielded by the Runge-Kutta 4 solution to either the scalar jerk or tangential jerk equations and the time-dependent curve calculated from kinematic equations. `curves.py` also has a feature that allows you to create an output file with all the data associated to the curve and the acceleration and jerk vectors, so you can further analyze the curves on your own. Running `hodograph.py` will launch a hodograph animation that represents the acceleration and jerk vectors moving along the curve. 

Both `curves.py` and `hodograph.py` have different features that give you control over the hodograph animation and the curves displayed, respectively. To interact with these features, you will have to change certain variables in the source code of `curves.py` and `hodograph.py` and then run the programs. Therefore, we recommend you install [Visual Studio Code](https://code.visualstudio.com), [PyCharm](https://www.jetbrains.com/pycharm/), or any other code editor in order to modify the programs' code easily and run them. Instructions on how to execute each program are provided below. 

### Instructions and examples
- [`curves.py - curve visualization`](https://github.com/MateoGitIt/constant-jerk-curve/wiki/How-to-use-curves.py-%7C-Curve-visualization)
- [`curves.py - output data file`](https://github.com/MateoGitIt/constant-jerk-curve/wiki/How-to-use-curves.py-%7C-Data-output-file)
- [`hodograph.py`](https://github.com/MateoGitIt/constant-jerk-curve/wiki/How-to-use-hodograph.py)

### Setting initial conditions

Like all numerically-simulated physical scenarios, our code requires initial physical conditions to run. The `inputParams.py` file contains __twelve__ variables that you may modify to indicate what the initial conditions are. All the variables are in SI units.
1. `JERK_MAGNITUDE` (integer or float): the magnitude of the scalar or tangential jerk.
2. `JERK_EQUATION` (string): the equation you would like to run Runge-Kutta 4 on (either the equation for scalar jerk or tangential jerk). Only accepted values are `"scalar"` or `"tangential"`.
3. `GRAVITATIONAL_ACCELERATION` (integer or float): the acceleration due to Earth's gravitational field (little g).
4. `INITIAL_ACCELERATION` (integer or float): the magnitude of acceleration at time = 0.
5. `INITIAL_SPEED` (integer or float): the magnitude of the velocity at time = 0.
6. `INITIAL_HEIGHT` (integer or float): the magnitude of the position at time = 0.
7. `CURVE_HORIZONTAL_LENGTH` (integer or float): the length along the x axis of the curve; modifying this value makes the curve longer or shorter horizontally.
8. `TIME_DURATION` (integer or float): the amount of time for which to run the kinematics equations to simulate the kinematics-based curve.
9. `STEP_SIZE` (float < 1): the horizontal step size for running the RK4 simulation; recommended values 0.1 > dx > 0.001.
10. `TIME_INCREMENT` (float < 1): the time step size for running the kinematics simulation; recommended values 0.1 > dt > 0.001
11. `DECIMALS_TO_ROUND` (integer): the number of decimal places to round values output through the terminal and in the output CSV files.
12. `Q_FACTOR` (integer or float): the moment of inertia factor (set to `1` if the object is not rolling).


