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
As a user, there are two primary ways to interact with our code: by running `curves.py` or `hodograph.py`. Running `curves.py` will allow you to visualize two curves: the curve yielded by the Runge-Kutta-4 solution to the (jerk differential equation? how do we want to call/point to that equation?) and the time-dependent curve calculated from kinematic equations. Running 
