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

Both `curves.py` and `hodograph.py` have different features that give you control over the hodograph animation and the curves displayed, respectively. To interact with these features, you will have to change certain variables in the source code of `curves.py` and `hodograph.py` and then run the programs. Therefore, we recommend you install [Visual Studio Code](https://code.visualstudio.com), [PyCharm](https://www.jetbrains.com/pycharm/), or any other code editor in order to modify the programs' code and run them through a command-line terminal.

### `curves.py`
The `curves.py` file has six variables you can modify to control different characteristics of the plot produced.

- `VIEW` (True/False bool): indicate whether to manually adjust the view of the plot. If set to `False`, the code will automatically set a default view of plot.
  
- `VIEW_BOUNDS` (Python list): If `VIEW` is set to `True`, then you can provide the bounds of the view frame by writing `VIEW_BOUNDS = [x1, x2, y1, y2]`. `x1` and `y1` are the lower x and y limits of the plot, while `x2` and `y2` are the upper limits.
  
- `ADD_DIVERGENCE_MOTION` (True/False bool): If set to `True`, the parabolic free fall motion after the object's trajectory diverges from the curve will be displayed in the plot. The point at which the object stops being in contact with the curve will be marked by a dark **X**. The object's location, speed, and acceleration at the divergence point will be printed to the terminal. If set to `False`, the free fall trajectory will not be displayed.

- `ADD_TEXTBOX` (True/False bool): 

- 
- `ADD_BEST_FIT` (True/False bool):
- `BEST_FIT_MODELS` (Python dictionary): 

<img width="1440" alt="curves py example 1" src="https://github.com/MateoGitIt/constant-jerk-curve/assets/96802084/43ac9d3e-a836-4bd1-b500-159c833c233a">

  




