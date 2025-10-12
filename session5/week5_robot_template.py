"""
This module is designed to display customizable robots using the tkinter GUI library. It reads robot configuration data from a JSON file, including colors and shapes for different parts of the robots, and then draws these robots on a canvas. The robots' appearance, such as body and antenna colors, can change based on certain conditions defined in the code.

Imports:
- tkinter: Used for creating the GUI elements and canvas for drawing robots.
- json: Used for loading robot configuration data from a JSON file.
"""


import tkinter as tk
import json


def make_print_status(status_text):
    """
    This function takes a string `status_text` as input and prints a formatted message indicating the successful creation of the given `status_text`.

    Args:
        status_text (str): The text to be printed as part of the success message.

    Returns:
        None
    """
    print(f'Successfully created: {status_text}')

def determine_body_color(i, colors, condition):
    """
    This function determines the body color of a robot based on the given condition and the colors dictionary.

    Args:
        i (int): The index of the robot being processed.
        colors (dict): A dictionary containing color information for each robot.
        condition (bool): A boolean condition to be evaluated for determining the body color.

    Returns:
        str: The color string representing the body color of the robot.
    """
    if condition:
        return colors[f"robot{i + 1}"]["body_color"]
    else:
        return "gray"

def determine_antenna_color(i, colors, config, my_th):
    """
    This function determines the antenna color of a robot based on its center_x coordinate and a threshold value.

    Args:
        i (int): The index of the robot being processed.
        colors (dict): A dictionary containing color information for each robot.
        config (dict): A dictionary containing configuration data for the current robot.
        my_th (int or float): A threshold value to compare the robot's center_x coordinate against.

    Returns:
        str: The color string representing the antenna color of the robot.
    """
    if config["center_x"] >= my_th:
        return "purple"
    else:
        return colors[f"robot{i + 1}"]["light_color"]

def draw_robot(i, canvas, config, colors, body_color, antenna_color):
    """
    This function draws a robot on the given canvas with the specified body color, antenna color, and configuration data.

    Args:
        i (int): The index of the robot being processed.
        canvas (tk.Canvas): The Tkinter canvas object on which to draw the robot.
        config (dict): A dictionary containing configuration data for the current robot.
        colors (dict): A dictionary containing color information for each robot.
        body_color (str): The color string representing the body color of the robot.
        antenna_color (str): The color string representing the antenna color of the robot.

    Returns:
        None
    """
    constant_val = 0
    canvas.create_polygon(config['robot_points'], fill=body_color, tags='robot')
    canvas.create_oval(config["center_x"] - 0, config["center_y"] - 0, config["center_x"] + 0, config["center_y"] + 0, fill=antenna_color, tags='robot')
    canvas.create_oval(config["wheel1_x"] - constant_val, config["wheel1_y"] - constant_val, config["wheel1_x"] + constant_val, config["wheel1_y"] + constant_val, fill=colors[f"robot{i + 1}"]["wheel_color_left"], tags='robot')
    canvas.create_oval(config["wheel2_x"] - constant_val, config["wheel2_y"] - constant_val, config["wheel2_x"] + constant_val, config["wheel2_y"] + constant_val, fill=colors[f"robot{i + 1}"]["wheel_color_right"], tags='robot')
    canvas.create_oval(config["sensor1_x"] - constant_val, config["sensor1_y"] - constant_val, config["sensor1_x"] + constant_val, config["sensor1_y"] + constant_val, fill=colors[f"robot{i + 1}"]["sensor_color"], tags='robot')
    canvas.create_oval(config["sensor2_x"] - constant_val, config["sensor2_y"] - constant_val, config["sensor2_x"] + constant_val, config["sensor2_y"] + constant_val, fill=colors[f"robot{i + 1}"]["sensor_color"], tags='robot')
    text_x = config["center_x"] + 40
    text_y = config["center_y"]
    canvas.create_text(text_x, text_y, text=config["label"], anchor=tk.W)
    make_print_status(config["label"])

def create_robot(i, canvas, config, condition, colors, my_th):
    """
    This function creates a robot on the given canvas by determining its body color, antenna color, and drawing it based on the provided configuration data, colors, and conditions.

    Args:
        i (int): The index of the robot being processed.
        canvas (tk.Canvas): The Tkinter canvas object on which to draw the robot.
        config (dict): A dictionary containing configuration data for the current robot.
        condition (bool): A boolean condition to be evaluated for determining the body color.
        colors (dict): A dictionary containing color information for each robot.
        my_th (int or float): A threshold value to compare the robot's center_x coordinate against for determining the antenna color.

    Returns:
        None
    """
    body_color = determine_body_color(i, colors, condition)
    antenna_color = determine_antenna_color(i, colors, config, my_th)
    draw_robot(i, canvas, config, colors, body_color, antenna_color)

def load_robot_data(filepath):
    """
    This function loads robot data from a JSON file specified by the given file path.

    Args:
        filepath (str): The path to the JSON file containing the robot data.

    Returns:
        dict: A dictionary containing the loaded robot data.
    """
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
    return data

def initialize_robots(canvas, data):
    """
    This function initializes and creates robots on the given canvas based on the provided robot data.

    Args:
        canvas (tk.Canvas): The Tkinter canvas object on which to draw the robots.
        data (dict): A dictionary containing the robot data, including colors and robot configurations.

    Returns:
        None
    """
    colors = data["colors"]
    robot_configurations = data["robot_configurations"]
    condition = True
    my_th = 500
    for i, config in enumerate(robot_configurations):
        create_robot(i, canvas, config, condition, colors, my_th)

def setup_application():
    """
    This function sets up the Tkinter application window and canvas for displaying the robots.

    Returns:
        Tuple[tk.Tk, tk.Canvas]: A tuple containing the Tkinter root window and canvas objects.
    """
    root = tk.Tk()
    root.title("Customizable Robots")
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()
    return root, canvas

def main():
    """
    The main function of the program. It sets up the application, loads the robot data, and initializes the robots on the canvas.
    """
    root, canvas = setup_application()
    data = load_robot_data('../robot_data.json')
    initialize_robots(canvas, data)
    root.mainloop()

if __name__ == "__main__":
    main()