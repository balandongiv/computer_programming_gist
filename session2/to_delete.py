import tkinter as tk
a = 10
b = a
a = 3
print(b)

# Create a tkinter window
root = tk.Tk()
root.title("Customizable Robots")

# Prevent the window from being resizable
root.resizable(False, False)

# Create a canvas widget within the window
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Define colors for different parts of the robots
wheel_color_left = "red" # string
wheel_color_right = "green"
sensor_color = "gold"
light_color = "yellow"
body_color = "blue"

# Define points to create the robot's shape
## Robot 1 point properties
robot1_points = [
    293.9,          # numeric
    478.4,
    300.4, 538.1,
    360.1, 531.6,
    353.6, 471.9,
]

## Robot 2 point properties
# robot2_points = [???????]

robot2_points = [
    593.9, 478.4,
    600.4, 538.1,
    660.1, 531.6,
    653.6, 471.9,
]


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
center_x2 = 627
center_y2 = 505
wheel1_x2 = 630.3
wheel1_y2 = 534.8
wheel2_x2 = 623.7
wheel2_y2 = 475.2
sensor1_x2 = 654.6
sensor1_y2 = 481.8
sensor2_x2 = 659.0
sensor2_y2 = 521.6


# Constants for component size
constant_val = 3


# Create the robots on the canvas

## Robot 1
canvas.create_polygon(robot1_points, fill=body_color, tags='robot')
canvas.create_oval(center_x1 - 10, center_y1 - 10, center_x1 + 10, center_y1 + 10, fill=light_color, tags='robot')


# Robot 1 wheel
canvas.create_oval(wheel1_x1 - constant_val, wheel1_y1 - constant_val, wheel1_x1 + constant_val, wheel1_y1 + constant_val, fill=wheel_color_left, tags='robot')
canvas.create_oval(wheel2_x1 - constant_val, wheel2_y1 - constant_val, wheel2_x1 + constant_val, wheel2_y1 + constant_val, fill=wheel_color_right, tags='robot')



# Right Sensor properties
canvas.create_oval(sensor1_x1 - constant_val, sensor1_y1 - constant_val, sensor1_x1 + constant_val, sensor1_y1 + constant_val, fill=sensor_color, tags='robot')
canvas.create_oval(sensor2_x1 - constant_val, sensor2_y1 - constant_val, sensor2_x1 + constant_val, sensor2_y1 + constant_val, fill=sensor_color, tags='robot')



## Robot 2
# Create robot components on the canvas for robot 2

canvas.create_polygon(robot2_points, fill=body_color, tags='robot')
canvas.create_oval(center_x2 - 8, center_y2 - 8, center_x2 + 8, center_y2 + 8, fill=light_color, tags='robot')

# Create robot components on the canvas for robot 2
canvas.create_oval(wheel1_x2 - constant_val, wheel1_y2 - constant_val, wheel1_x2 + constant_val, wheel1_y2 + constant_val, fill=wheel_color_left, tags='robot')
canvas.create_oval(wheel2_x2 - constant_val, wheel2_y2 - constant_val, wheel2_x2 + constant_val, wheel2_y2 + constant_val, fill=wheel_color_right, tags='robot')
canvas.create_oval(sensor1_x2 - constant_val, sensor1_y2 - constant_val, sensor1_x2 + constant_val, sensor1_y2 + constant_val, fill=sensor_color, tags='robot')
canvas.create_oval(sensor2_x2 - constant_val, sensor2_y2 - constant_val, sensor2_x2 + constant_val, sensor2_y2 + constant_val, fill=sensor_color, tags='robot')


# Main tkinter event loop
root.mainloop()