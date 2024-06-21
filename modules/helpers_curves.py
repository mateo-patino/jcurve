from modules.rungekutta import rungekutta_main
from modules.simulated import simulated_main
from modules.components import tangential_accel2, normal_accel2, tangential_jerk, normal_jerk, components_file_local_copy
from modules.computations import local_angle
from math import degrees
from inputParams import parameters
import numpy as np
import pandas as pd
import csv

Jt, Jf, Q, g, a0, v0, y0, xmax, tmax, h, dt, rounding_decimals = parameters.values()

def verify_view_bounds(bounds):
    for b in bounds:
        if not isinstance(b, int) and not isinstance(b, float):
            exit("All bounds must integers or floating-point values.")
    if bounds[0] < bounds[1] and bounds[2] < bounds[3]:
        return bounds
    else:
        exit("Bounds are incorrect. Accepted format is [x1,x2,y1,y2] where x1 and y1 must "
             "be less than x2 and y2, respectively.")


def compute_curves():
    try:
        rk_X, rk_Y, U = rungekutta_main()
        kin_X, kin_Y = simulated_main()
    except Exception as e:
        print(f"An error ocurred calculating the curves with the initial conditions provided: {e}. "
              "Physically impossible initial conditions may cause some equations to break down. " 
              "Try different initial conditions.")
        exit()
    return {"rk4": [rk_X, rk_Y], "kinematics": [kin_X, kin_Y], "u_values": U}


def export_data(output_filename, file_format, data, vector_data, progress):
    tang_norm_components = {}
    if vector_data:
        components_file_local_copy(data["u_values"], data["rk4"][1], data["rk4"][0])
        tang_norm_components = output_vector_data(data["rk4"][1], data["u_values"], progress)
    if file_format == "xlsx":
        write_xlsx(output_filename, {**format_rk_data(data), **tang_norm_components}, progress)
    elif file_format == "csv":
        write_csv(output_filename, {**format_rk_data(data), **tang_norm_components}, progress)


def write_xlsx(filename, data, progress):
    if progress: print(f"Writing data to {filename}. After the bar reaches 100%, you may have to wait for a moment.")
    else: print(f"Writing data to {filename}. You may have to wait for a moment or even a couple of minutes if "
                "you requested vector data or used a small step size to compute the curve.")
    df = pd.DataFrame(data)
    total_rows = len(df)
    chunk_size = max(1, total_rows // 100)
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        for i in range(0, total_rows, chunk_size):
            end_row = min(i + chunk_size, total_rows)
            chunk_df = df.iloc[i:end_row]
            chunk_df.to_excel(writer, startrow=i, index=False, header=(i == 0))
            if progress: progress_bar(i + chunk_size, total_rows)


def write_csv(filename, data, progress):
    data_points = len(data["rk_X"])
    with open(filename, "w") as f:
        fieldnames = data.keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        print(f"\nWriting data to {filename}...")
        for i in range(data_points):
            if progress: progress_bar(i + 1, data_points)
            row = {}
            for key, value in data.items():
                row[key] = round(value[i], rounding_decimals)
            writer.writerow(row)
        print()

def format_rk_data(data):
    angle_data = np.array([degrees(local_angle(u)) for u in data["u_values"]])
    result = {
        "rk_X": data["rk4"][0],
        "rk_y": data["rk4"][1],
        "U": data["u_values"],
        "angle": angle_data
    }
    return result


def output_vector_data(Y, U, progress):
    data_points = len(Y)
    tang_accel, tang_accel_x, tang_accel_y, norm_accel, norm_accel_x, norm_accel_y = [np.empty(data_points) for _ in range(6)]
    tang_jerk, tang_jerk_x, tang_jerk_y, norm_jerk, norm_jerk_x, norm_jerk_y = [np.empty(data_points) for _ in range(6)]
    print(f"Calculating vector data for exporting ({12 * data_points} total values)...")
    for i in range(data_points):
        if progress: progress_bar(i + 1, data_points)
        tang_accel_components, tang_accel_magn = tangential_accel2(U[i], Y[i])
        tang_accel[i] = tang_accel_magn
        tang_accel_x[i], tang_accel_y[i] = tang_accel_components
        norm_accel_components, norm_accel_magn = normal_accel2(U[i], Y[i])
        norm_accel[i] = norm_accel_magn
        norm_accel_x[i], norm_accel_y[i] = norm_accel_components
        tang_jerk_components, tang_jerk_magn = tangential_jerk(U[i], Y[i])
        tang_jerk[i] = tang_jerk_magn
        tang_jerk_x[i], tang_jerk_y[i] = tang_jerk_components
        norm_jerk_components, norm_jerk_magn = normal_accel2(U[i], Y[i])
        norm_jerk[i] = norm_jerk_magn
        norm_jerk_x[i], norm_jerk_y[i] = norm_jerk_components
    print()
    vector_data = {"tang_accel": tang_accel, "tang_accel_x": tang_accel_x, "tang_accel_y": tang_accel_y,
                   "norm_accel": norm_accel, "norm_accel_x": norm_accel_x, "norm_accel_y": norm_accel_y,
                   "tang_jerk": tang_jerk, "tang_jerk_x": tang_jerk_x, "tang_jerk_y": tang_jerk_y,
                   "norm_jerk": norm_jerk, "norm_jerk_x": norm_jerk_x, "norm_jerk_y": norm_jerk_y}
    return vector_data


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * int(100 - percent)
    print(f"\r| {bar} | {round(percent)}%", end='\r')
