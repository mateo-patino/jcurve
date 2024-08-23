# PROVIDE THE INITIAL PHYSICAL CONDITIONS FOR SIMULATING THE CONSTANT-JERK CURVE. 
JERK_MAGNITUDE = 0.5
JERK_EQUATION = "scalar"
GRAVITATIONAL_ACCELERATION = 9.81
INITIAL_ACCELERATION = 0.1
INITIAL_SPEED = 1
INITIAL_HEIGHT = 300
CURVE_HORIZONTAL_LENGTH = 375
TIME_DURATION = 19
STEP_SIZE = 0.01
TIME_INCREMENT = 0.01
DECIMALS_TO_ROUND = 5
Q_FACTOR = 1

if JERK_MAGNITUDE <= 0: jerkfactor = 1
else: jerkfactor = -1

parameters = {"j_t":  JERK_MAGNITUDE, 
              "jerk_eq": JERK_EQUATION,
              "j_f": jerkfactor,
              "Q": Q_FACTOR, 
              "g": GRAVITATIONAL_ACCELERATION, 
              "a_0": INITIAL_ACCELERATION, 
              "v_0": INITIAL_SPEED, 
              "y_0": INITIAL_HEIGHT, 
              "xmax": CURVE_HORIZONTAL_LENGTH,
              "tmax": TIME_DURATION,
              "h": STEP_SIZE,
              "dt": TIME_INCREMENT,
              "rounding_decimals": DECIMALS_TO_ROUND}

