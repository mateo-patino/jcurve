from modules.helpers import create_plot, divergence_point, create_fit_curve
from modules.helpers_curves import verify_view_bounds, compute_curves, export_data
import matplotlib.pyplot as plt

# CURVE VISUALIZATION
VIEW_BOUNDS = [0, 800, -500, 300]
VIEW = True
ADD_DIVERGENCE_MOTION = True
ADD_TEXTBOX = True
ADD_BEST_FIT = True
BEST_FIT_MODELS = {"5_poly": [1, 1, 1, 1, 1, 1]}

# OUTPUT FILE OPTION
CREATE_OUTPUT_FILE = False
ADD_VECTOR_DATA = True
ADD_PROGRESS_BAR = True
OUTPUT_FILENAME = "test"
OUTPUT_FILE_FORMAT = "xlsx"

fig, axs = plt.subplots(1, 2)
data = compute_curves()
div_data = divergence_point(data["rk4"][0], data["rk4"][1], data["u_values"])
plots = ["rk4", "kinematics"]

for i, ax in enumerate(axs):
    create_plot(plots[i], ax, data=data[plots[i]], div=(ADD_DIVERGENCE_MOTION, *div_data), view=(VIEW, *verify_view_bounds(VIEW_BOUNDS)),
                show_textbox=ADD_TEXTBOX)
    if ADD_BEST_FIT:
        for model in list(BEST_FIT_MODELS.keys()):
            create_fit_curve(model, ax, BEST_FIT_MODELS[model], VIEW_BOUNDS[0], VIEW_BOUNDS[1], data=data[plots[i]], curve_tag=plots[i])
    ax.legend()

if CREATE_OUTPUT_FILE:
    export_data(f"{OUTPUT_FILENAME}.{OUTPUT_FILE_FORMAT}", OUTPUT_FILE_FORMAT, data, ADD_VECTOR_DATA, ADD_PROGRESS_BAR)

plt.show()