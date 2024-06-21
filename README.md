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
