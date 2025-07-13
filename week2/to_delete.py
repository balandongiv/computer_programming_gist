import tkinter as tk
import json

# Configuration and Data Loading
try:
    with open('../robot_data.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("Error: robot_data.json not found.")
    exit()  # Exit the program gracefully if the file is not found

colors = data.get("colors", {}) # Handle the case where colors might not be in the json
robot_configurations = data.get("robot_configurations", [])  # Safeguard against missing configurations

# --- Tkinter Setup ---
root = tk.Tk()
root.title("Customizable Robots")
root.resizable(False, False)
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# --- Robot Drawing ---
condition = True  # This could be made dynamic/configurable
threshold = 500  # This could be made dynamic/configurable
constant_val = 0  # Consider renaming this for better clarity (e.g., wheel_radius)

for i, config in enumerate(robot_configurations):
    robot_id = i + 1
    robot_colors = colors.get(f"robot{robot_id}", {}) # Get colors for this robot or an empty dict if not defined

    # Body Color Logic
    body_color = robot_colors.get("body_color", "gray") if condition else "gray"

    # Antenna Color Logic
    antenna_color = "purple" if config["center_x"] >= threshold else robot_colors.get("light_color", "gray")

    # Drawing the Robot
    canvas.create_polygon(config['robot_points'], fill=body_color, tags='robot')
    canvas.create_oval(config["center_x"], config["center_y"], config["center_x"], config["center_y"], fill=antenna_color, tags='robot') # Antenna (currently 0 size)

    # Wheels, Sensors (Using robot_colors or gray if not specified)
    canvas.create_oval(config["wheel1_x"] - constant_val, config["wheel1_y"] - constant_val, config["wheel1_x"] + constant_val, config["wheel1_y"] + constant_val, fill=robot_colors.get("wheel_color_left", "gray"), tags='robot')
    canvas.create_oval(config["wheel2_x"] - constant_val, config["wheel2_y"] - constant_val, config["wheel2_x"] + constant_val, config["wheel2_y"] + constant_val, fill=robot_colors.get("wheel_color_right", "gray"), tags='robot')
    canvas.create_oval(config["sensor1_x"] - constant_val, config["sensor1_y"] - constant_val, config["sensor1_x"] + constant_val, config["sensor1_y"] + constant_val, fill=robot_colors.get("sensor_color", "gray"), tags='robot')
    canvas.create_oval(config["sensor2_x"] - constant_val, config["sensor2_y"] - constant_val, config["sensor2_x"] + constant_val, config["sensor2_y"] + constant_val, fill=robot_colors.get("sensor_color", "gray"), tags='robot')

    # Label
    canvas.create_text(config["center_x"] + 40, config["center_y"], text=config["label"], anchor=tk.W)
    print(f'Successfully created: {config["label"]}')



# --- Tkinter Main Loop ---
root.mainloop()