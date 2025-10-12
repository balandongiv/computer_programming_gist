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

        # TASK 1: Complete the Position and Shape Configuration .
        # Below is the incomplete version for the robot configuration.
        # You can complete the rest of the configuration by referring to the robot_data.json file.
        # self.center_x = robot_configuration["?????"]
        # self.????= robot_configuration["center_y"]
        # self.wheel1_x = robot_configuration["?????"]
        # self.wheel1_y = robot_configuration["?????"]
        # self.wheel2_x = robot_configuration["?????"]
        # self.wheel2_y = robot_configuration["?????"]
        # self.????? = robot_configuration["sensor1_x"]
        # self.?????= robot_configuration["sensor1_y"]
        # self.????? = robot_configuration["sensor2_x"]
        # self.sensor2_y = robot_configuration["sensor2_y"]
        # self.robot_points = robot_configuration["robot_points"]
        self.label = robot_configuration["label"]
        self.canvas = canvasp



    # TASK 3a: Implement the draw robot Method
    def draw_robot(self):
        pass
        # canvas.create_polygon(points, fill="blue", tags=self.name)


    # TASK 2b: Adding the str Method to the Bot Class
    # def __str__(self):



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
    data = load_robot_data('../helper/robot_data.json')

    robot_one = Bot(canvas,
                    color=data['colors']['robot1'],
                    robot_configuration=data['robot_configurations'][0])

    # TASK 2a: Adding the str Method to the Bot Class
    # print(robot_one)

    # TASK 3b: Implement the draw robot Method
    # robot_one.draw_robot()

    # print(robot_one.light_color)

    # TASK 4: Create a Second Robot Object - robot two
    # bot2 = registerBot("bot2",canvas)
    # bot2.draw(canvas)

    # TASK 3c: Implement the draw robot Method
    # root.mainloop()

if __name__ == "__main__":
    main()