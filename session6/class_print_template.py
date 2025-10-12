import tkinter as tk
import json

class Bot:

    def __init__(self,
                 canvasp,
                 color=None,
                 robot_configuration=None):
        self.wheel_color_left = color["wheel_color_left"]
        self.wheel_color_right = color["wheel_color_right"]
        self.sensor_color = color["sensor_color"]
        self.light_color = color["light_color"]
        self.body_color = color["body_color"]

        # Below is the incomplete version for the robot configuration.
        # You can complete the rest of the configuration by referring to the robot_data.json file.

        # self.center_x = robot_configuration["center_x"]
        # self.center_y = robot_configuration["center_y"]
        # self.wheel1_x = robot_configuration["wheel1_x"]
        # self.wheel1_y = robot_configuration["wheel1_y"]
        # self.wheel2_x = robot_configuration["wheel2_x"]
        # self.wheel2_y = robot_configuration["wheel2_y"]
        # self.sensor1_x = robot_configuration["sensor1_x"]
        # self.sensor1_y = robot_configuration["sensor1_y"]
        # self.sensor2_x = robot_configuration["sensor2_x"]
        # self.sensor2_y = robot_configuration["sensor2_y"]
        self.label = robot_configuration["label"]
        # self.robot_points = robot_configuration["robot_points"]

        self.canvas = canvasp



        # self.canvas = canvasp
    def draw_robot(self):
        pass
    def __str__(self):
        return f"This is the container for {self.label}"

def setup_application():

    root = tk.Tk()
    root.title("Customizable Robots")
    root.resizable(False, False)
    canvas = tk.Canvas(root, width=1000, height=1000)
    canvas.pack()
    return root, canvas

def load_robot_data(filepath):

    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
    return data

def main():
    root, canvas = setup_application()
    data = load_robot_data('../robot_data.json')

    robot_one = Bot(canvas,
                    color=data['colors']['robot1'],
                    robot_configuration=data['robot_configurations'][0])
    print(robot_one) # Ask student to print the value for light_color



if __name__ == "__main__":
    main()
