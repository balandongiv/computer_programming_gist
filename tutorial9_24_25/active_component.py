import math

import numpy as np

np.random.seed(12345)

class Bot:
    def __init__(self, name, canvas):
        self.x = np.random.randint(100, 900)
        self.y = np.random.randint(100, 900)
        self.theta = np.random.uniform(0.0, 2.0 * math.pi)
        self.name = name
        self.axle_length = 60
        self.left_velocity = 0.0
        self.right_velocity = 0.0
        self.battery = 1000
        self.turning = 0
        self.moving = np.random.randint(50, 101)
        self.is_turning = False
        self.canvas = canvas

    def draw(self, canvas):
        angle = np.pi / 2.0
        points = [
            (self.x + 30 * np.sin(self.theta)) - 30 * np.sin((angle) - self.theta),
            (self.y - 30 * np.cos(self.theta)) - 30 * np.cos((angle) - self.theta),
            (self.x - 30 * np.sin(self.theta)) - 30 * np.sin((angle) - self.theta),
            (self.y + 30 * np.cos(self.theta)) - 30 * np.cos((angle) - self.theta),
            (self.x - 30 * np.sin(self.theta)) + 30 * np.sin((angle) - self.theta),
            (self.y + 30 * np.cos(self.theta)) + 30 * np.cos((angle) - self.theta),
            (self.x + 30 * np.sin(self.theta)) + 30 * np.sin((angle) - self.theta),
            (self.y - 30 * np.cos(self.theta)) + 30 * np.cos((angle) - self.theta),
            ]
        canvas.create_polygon(points, fill="blue", tags=self.name)

        self.sensor_positions = [ # Renamed for clarity and PEP 8 style
            (self.x + 20 * np.sin(self.theta)) + 30 * np.sin((math.pi / 2.0) - self.theta),
            (self.y - 20 * np.cos(self.theta)) + 30 * np.cos((math.pi / 2.0) - self.theta),
            (self.x - 20 * np.sin(self.theta)) + 30 * np.sin((math.pi / 2.0) - self.theta),
            (self.y + 20 * np.cos(self.theta)) + 30 * np.cos((math.pi / 2.0) - self.theta),
            ]

        center_x = self.x
        center_y = self.y
        canvas.create_oval(center_x - 15, center_y - 15,
                           center_x + 15, center_y + 15,
                           fill="gold", tags=self.name)

        canvas.create_text(self.x, self.y, text=str(self.battery), tags=self.name)

        wheel1_x = self.x - 30 * math.sin(self.theta)
        wheel1_y = self.y + 30 * math.cos(self.theta)
        canvas.create_oval(wheel1_x - 3, wheel1_y - 3,
                           wheel1_x + 3, wheel1_y + 3,
                           fill="red", tags=self.name)

        wheel2_x = self.x + 30 * math.sin(self.theta)
        wheel2_y = self.y - 30 * math.cos(self.theta)
        canvas.create_oval(wheel2_x - 3, wheel2_y - 3,
                           wheel2_x + 3, wheel2_y + 3,
                           fill="green", tags=self.name)

        sensor1_x = self.sensor_positions[0]
        sensor1_y = self.sensor_positions[1]
        sensor2_x = self.sensor_positions[2]
        sensor2_y = self.sensor_positions[3]
        canvas.create_oval(sensor1_x - 3, sensor1_y - 3,
                           sensor1_x + 3, sensor1_y + 3,
                           fill="yellow", tags=self.name)
        canvas.create_oval(sensor2_x - 3, sensor2_y - 3,
                           sensor2_x + 3, sensor2_y + 3,
                           fill="yellow", tags=self.name)