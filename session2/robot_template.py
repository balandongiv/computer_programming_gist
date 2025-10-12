import tkinter as tk
# ket see if this works: i delete the fas and add this
# Create a tkinter window
root = tk.Tk()
root.title("Customizable Robots")

# Prevent the window from being resizable
root.resizable(False, False)

# Create a canvas widget within the window
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Define colors for different parts of the robots
wheel_color_left = "red"
wheel_color_right = "green"
sensor_color = "gold"
light_color = "yellow"
body_color = "blue"

constant_val=3
# Define points to create the robot's shape
## Robot 1 point properties
robot1_points = [
    293.9, 478.4,
    300.4, 538.1,
    360.1, 531.6,
    353.6, 471.9,
]

## Robot 2 point properties
# robot2_points = [???????]

# Define positions for various robot components
## positions for robot 1 components
center_x1 = 327
center_y1 = 505
wheel1_x1 = 330.3
wheel1_y1 = 534.8
wheel2_x1 = 323.7
wheel2_y1 = 475.2
sensor1_x1 = 354.6
sensor1_y1 = 481.8
sensor2_x1 = 359.0
sensor2_y1 = 521.6

## positions for robot 2 components
# center_x2,center_y2,wheel1_x2,wheel1_y2,wheel2_x2,wheel2_y2,sensor1_x2,sensor1_y2,sensor2_x2,sensor2_y2


# Create the robots on the canvas

## Robot 1
canvas.create_polygon(robot1_points, fill=body_color, tags='robot')
canvas.create_oval(center_x1 - 50, center_y1 -50, center_x1 + 8, center_y1 + 8, fill=light_color, tags='robot')
# Robot 1 wheel
canvas.create_oval(wheel1_x1 - 50, wheel1_y1 - 20, wheel1_x1 + 20, wheel1_y1 + 20, fill=wheel_color_right, tags='robot')
canvas.create_oval(wheel2_x1 - 20, wheel2_y1 - 20, wheel2_x1 + 20, wheel2_y1 + 20, fill=wheel_color_left, tags='robot')

# Right Sensor properties
canvas.create_oval(sensor1_x1 - 10, sensor1_y1 - 10, sensor1_x1 + 10, sensor1_y1 + 10, fill=sensor_color, tags='robot')
canvas.create_oval(sensor2_x1 - 3, sensor2_y1 - 3, sensor2_x1 + 3, sensor2_y1 + 3, fill=sensor_color, tags='robot')

## Robot 2


# Add text next to the robots


# Main tkinter event loop
root.mainloop()