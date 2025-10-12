import tkinter as tk

from helper.virtual_display import ensure_virtual_display

# Create a tkinter window
ensure_virtual_display()
root = tk.Tk()
root.title("Customizable Robots")

# Prevent the window from being resizable
root.resizable(False, False)

# Create a canvas widget within the window
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

# Define a dictionary of color sets for different parts of the robots

colors = dict(                          # Start of the colors dictionary
    robot1=dict(                        # Start of the robot1 dictionary
        wheel_color_left="red",
        wheel_color_right="green",
        sensor_color="gold",
        light_color="yellow",
        body_color="blue",
    ),  # End of the robot1 dictionary
    robot2=dict(                    # Start of the robot2 dictionary# Start of the robot2 dictionary
        wheel_color_left="orange",
        wheel_color_right="purple",
        sensor_color="silver",
        light_color="pink",
        body_color="cyan",
    ),  # End of the robot2 dictionary
)  # End of the colors dictionary

# Define a list of robot configurations

# List start
robot_configurations = [
    # Dictionary start
    dict(
        id="robot1",
        center_x=327,
        center_y=505,
        wheel1_x=330.3,
        wheel1_y=534.8,
        wheel2_x=323.7,
        wheel2_y=475.2,
        sensor1_x=354.6,
        sensor1_y=481.8,
        sensor2_x=359.0,
        sensor2_y=521.6,
        robot_points=[
            293.9, 478.4,
            300.4, 538.1,
            360.1, 531.6,
            353.6, 471.9,
        ]
    ),  # Dictionary end
    # Dictionary start
    dict(
        id="robot2",
        center_x=627,
        center_y=505,
        wheel1_x=630.3,
        wheel1_y=534.8,
        wheel2_x=623.7,
        wheel2_y=475.2,
        sensor1_x=654.6,
        sensor1_y=481.8,
        sensor2_x=659.0,
        sensor2_y=521.6,
        robot_points=[
            593.9, 478.4,
            600.4, 538.1,
            660.1, 531.6,
            653.6, 471.9,
        ]
    )  # Dictionary end
]  # List end



# Add a variable to control the condition
condition = True # You can change this condition as needed

# Create robots using a loop
constant_val = 10  # Adjusted to give some size to the components
for config in robot_configurations:
    robot_colors = colors[config["id"]]

    # Check the condition and change the body color accordingly
    body_color = robot_colors["body_color"] if condition else "black"

    # Create the robot on the canvas
    canvas.create_polygon(config['robot_points'], fill=body_color, tags='robot')

    # add your code here and below
    # Refer to last session code for creating the robot components


# Main tkinter event loop
root.mainloop()