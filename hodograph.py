from modules.helpers import divergence_point, create_hodograph, pause_hodograph, exit_hodograph
from modules.helpers_curves import verify_view_bounds, compute_curves
import matplotlib.pyplot as plt

# CHANGE THE FOLLOWING FIVE PARAMETERS TO CONTROL THE HODOGRAPH
VECTORS = [("accel", 50), ("jerk", 50)]
FRAMES = 750
PAUSE = 0.01
VIEW_BOUNDS = [0, 800, -400, 400]
DIVERGENCE_MOTION = True


fig, ax = plt.subplots(1, 1)
data = compute_curves()
div_data = divergence_point(data["rk4"][0], data["rk4"][1], data["u_values"])
colors = ["tab:orange", "tab:blue"]
fig.canvas.mpl_connect("close_event", exit_hodograph)
fig.canvas.mpl_connect("key_press_event", pause_hodograph)
create_hodograph("rk4", VECTORS, ax, data["rk4"][0], data["rk4"][1], U=data["u_values"], div=(DIVERGENCE_MOTION, *div_data),
                    frame_num=FRAMES, pause_length=PAUSE, view=verify_view_bounds(VIEW_BOUNDS), color_list=colors)

plt.show()