# Modelling a Constant-Jerk Curve 🎢
This repository contains code for "[paper title]." The Python scripts here implement a tool to visualize the constant-jerk _y=y(x)_ curve presented in the paper. A hodograph of the jerk and acceleration vectors for an object traveling along the curve is also implemented.

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
As a user, there are two ways to interact with our code: by running `curves.py` or `hodograph.py`. Running `curves.py` will allow you to visualize two curves – the curve yielded by the Runge-Kutta-4 solution to the (*jerk differential equation? how do we want to call/point to that equation that we use RK4 on?*) and the time-dependent curve calculated from kinematic equations. Running `hodograph.py` will launch a hodograph animation that represents the acceleration and jerk vectors moving along the curve. 

Both `curves.py` and `hodograph.py` have different features that give you control over the hodograph animation and the curves displayed, respectively. To interact with these features, you will have to change certain variables in the source code of `curves.py` and `hodograph.py` and then run the programs. Therefore, we recommend you install [Visual Studio Code](https://code.visualstudio.com), [PyCharm](https://www.jetbrains.com/pycharm/), or any other code editor in order to modify the programs' code and run them through a command-line terminal. Instructions on how to execute each program are provided below.

### Instructions and examples
- [`curves.py`](https://github.com/MateoGitIt/constant-jerk-curve/wiki/How-to-use-curves.py)
- [`hodograph.py`](https://github.com/MateoGitIt/constant-jerk-curve/wiki/How-to-use-hodograph.py)

### Setting initial conditions

Like all numerically-simulated physical scenarios, our code requires initial physical conditions to run. The `inputParams.py` file contains __eleven__ variables that you may modify to indicate what the initial conditions are. 
1. `TANGENTIAL_JERK`: the tangential component of jerk which is to be held constant throughout the curve.
2. `GRAVITATIONAL_ACCELERATION`: the acceleration due to Earth's gravitational field (little g).
3. `INITIAL_ACCELERATION`: the magnitude of acceleration at time = 0.
4. `INITIAL_SPEED`: the magnitude of the velocity at time = 0.
5. `INITIAL_HEIGHT`: the magnitude of the position at time = 0.
6. `CURVE_HORIZONTAL_LENGTH`: the length along the x axis of the curve; modifying this value makes the curve longer or shorter horizontally.
7. `TIME_DURATION`: the amount of time for which to run the kinematics equations to simulate the kinematics-based curve.
8. `STEP_SIZE`: the horizontal step size for running the RK4 simulation; recommended values 0.1 > ss > 0.001.
9. `TIME_INCREMENT`: the time step size for running the kinematics simulation; recommended values 0.1 > dt > 0.001
10. `DECIMALS_TO_ROUND`: the number of decimal places to round values output through the terminal and in the output CSV files.
11. `Q_FACTOR:` the moment of inertia factor (set to `1` if the object is not rolling).


