import math
import random

import numpy as np
# from playsound import playsound

from cat import Cat
from passive_component import Dirt, Charger, WiFiHub


class Bot:

    def __init__(self, name, canvas):
        self.x = random.randint(100, 900)
        self.y = random.randint(100, 900)
        self.theta = random.uniform(0.0, 2.0 * math.pi)
        # self.theta = 0
        self.name = name
        self.axle_length = 60  # axle width
        self.velocity_left = 0.0
        self.velocity_right = 0.0
        self.battery = 1000
        self.turning_time = 0
        self.moving_time = random.randrange(50, 100)
        self.is_turning = False
        # self.map = np.zeros( (10,10) )
        self.canvas = canvas
        self.view = [0] * 9

    def draw(self, canvas):
        camera_positions = []
        for pos in range(20, -21, -5):
            camera_positions.append(((self.x + pos * math.sin(self.theta)) + 30 * math.sin((math.pi / 2.0) - self.theta),
                                     (self.y - pos * math.cos(self.theta)) + 30 * math.cos((math.pi / 2.0) - self.theta)))

        points = [(self.x + 30 * math.sin(self.theta)) - 30 * math.sin((math.pi / 2.0) - self.theta),
                  (self.y - 30 * math.cos(self.theta)) - 30 * math.cos((math.pi / 2.0) - self.theta),
                  (self.x - 30 * math.sin(self.theta)) - 30 * math.sin((math.pi / 2.0) - self.theta),
                  (self.y + 30 * math.cos(self.theta)) - 30 * math.cos((math.pi / 2.0) - self.theta),
                  (self.x - 30 * math.sin(self.theta)) + 30 * math.sin((math.pi / 2.0) - self.theta),
                  (self.y + 30 * math.cos(self.theta)) + 30 * math.cos((math.pi / 2.0) - self.theta),
                  (self.x + 30 * math.sin(self.theta)) + 30 * math.sin((math.pi / 2.0) - self.theta),
                  (self.y - 30 * math.cos(self.theta)) + 30 * math.cos((math.pi / 2.0) - self.theta)]
        canvas.create_polygon(points, fill="blue", tags=self.name)

        sensor_positions = [(self.x + 20 * math.sin(self.theta)) + 30 * math.sin((math.pi / 2.0) - self.theta),
                            (self.y - 20 * math.cos(self.theta)) + 30 * math.cos((math.pi / 2.0) - self.theta),
                            (self.x - 20 * math.sin(self.theta)) + 30 * math.sin((math.pi / 2.0) - self.theta),
                            (self.y + 20 * math.cos(self.theta)) + 30 * math.cos((math.pi / 2.0) - self.theta)]

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

        sensor1_x = sensor_positions[0]
        sensor1_y = sensor_positions[1]
        sensor2_x = sensor_positions[2]
        sensor2_y = sensor_positions[3]
        canvas.create_oval(sensor1_x - 3, sensor1_y - 3,
                           sensor1_x + 3, sensor1_y + 3,
                           fill="yellow", tags=self.name)
        canvas.create_oval(sensor2_x - 3, sensor2_y - 3,
                           sensor2_x + 3, sensor2_y + 3,
                           fill="yellow", tags=self.name)

        for x, y in camera_positions:
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="purple1", tags=self.name)
        for x, y in camera_positions:
            canvas.create_line(x, y, x + 400 * math.cos(self.theta), y + 400 * math.sin(self.theta), fill="light grey",
                               tags=self.name)
        self.camera_positions = camera_positions
        self.sensor_positions = sensor_positions

    # cf. Dudek and Jenkin, Computational Principles of Mobile Robotics
    def move(self, canvas, registry_passives, dt):
        if self.battery > 0:
            self.battery -= 1
        if self.battery == 0:
            self.velocity_left = 0
            self.velocity_right = 0
        for rr in registry_passives:
            if isinstance(rr, Charger) and self.distance_to(rr) < 80:
                self.battery += 10

        if self.velocity_left == self.velocity_right:
            r = 0
        else:
            r = (self.axle_length / 2.0) * ((self.velocity_right + self.velocity_left) / (
                    self.velocity_left - self.velocity_right))
        omega = (self.velocity_left - self.velocity_right) / self.axle_length
        icc_x = self.x - r * math.sin(self.theta)  # instantaneous centre of curvature
        icc_y = self.y + r * math.cos(self.theta)
        m = np.matrix([[math.cos(omega * dt), -math.sin(omega * dt), 0],
                       [math.sin(omega * dt), math.cos(omega * dt), 0],
                       [0, 0, 1]])
        v1 = np.matrix([[self.x - icc_x], [self.y - icc_y], [self.theta]])
        v2 = np.matrix([[icc_x], [icc_y], [omega * dt]])
        new_v = np.add(np.dot(m, v1), v2)
        new_x = new_v.item(0)
        new_y = new_v.item(1)
        new_theta = new_v.item(2)
        new_theta = new_theta % (2.0 * math.pi)  # make sure angle doesn't go outside [0.0,2*pi)
        self.x = new_x
        self.y = new_y
        self.theta = new_theta
        if self.velocity_left == self.velocity_right:  # straight line movement
            self.x += self.velocity_right * math.cos(self.theta)  # vr wlog
            self.y += self.velocity_right * math.sin(self.theta)
        if self.x < 0.0:
            self.x = 999.0
        if self.x > 1000.0:
            self.x = 0.0
        if self.y < 0.0:
            self.y = 999.0
        if self.y > 1000.0:
            self.y = 0.0
        # self.updateMap()
        canvas.delete(self.name)
        self.draw(canvas)

    def look(self, registry_actives):
        self.view = [0] * 9
        for idx, pos in enumerate(self.camera_positions):
            for cc in registry_actives:
                if isinstance(cc, Cat):
                    distance = self.distance_to(cc)
                    scaled_distance = max(400 - distance, 0) / 400
                    ncx = cc.x - pos[0]  # cat if robot were at 0,0
                    ncy = cc.y - pos[1]
                    # print(abs(angle-self.theta)%2.0*math.pi)
                    m = math.tan(self.theta)
                    a = m * m + 1
                    b = 2 * (-m * ncy - ncx)
                    r = 15  # radius
                    c = ncy * ncy - r * r + ncx * ncx
                    if b * b - 4 * a * c >= 0 and scaled_distance > self.view[idx]:
                        self.view[idx] = scaled_distance
        self.canvas.delete("view")
        for vv in range(9):
            if self.view[vv] == 0:
                self.canvas.create_rectangle(850 + vv * 15, 50, 850 + vv * 15 + 15, 65, fill="white", tags="view")
            if self.view[vv] > 0:
                colour = hex(15 - math.floor(self.view[vv] * 16.0))  # scale to 0-15 -> hex
                fill_hex = "#" + colour[2] + colour[2] + colour[2]
                self.canvas.create_rectangle(850 + vv * 15, 50, 850 + vv * 15 + 15, 65, fill=fill_hex, tags="view")
        return self.view

    def pick_up_and_put_down(self, x, y):
        self.x = x
        self.y = y
        self.canvas.delete(self.name)
        self.draw(self.canvas)

    def sense_charger(self, registry_passives):
        light_left = 0.0
        light_right = 0.0
        for pp in registry_passives:
            if isinstance(pp, Charger):
                lx, ly = pp.get_location()
                distance_left = math.sqrt((lx - self.sensor_positions[0]) * (lx - self.sensor_positions[0]) +
                                          (ly - self.sensor_positions[1]) * (ly - self.sensor_positions[1]))
                distance_right = math.sqrt((lx - self.sensor_positions[2]) * (lx - self.sensor_positions[2]) +
                                           (ly - self.sensor_positions[3]) * (ly - self.sensor_positions[3]))
                light_left += 200000 / (distance_left * distance_left)
                light_right += 200000 / (distance_right * distance_right)
        return light_left, light_right

    def sense_hubs(self, registry_passives):
        signal = []
        for pp in registry_passives:
            if isinstance(pp, WiFiHub):
                lx, ly = pp.get_location()
                distance_left = math.sqrt((lx - self.sensor_positions[0]) * (lx - self.sensor_positions[0]) +
                                          (ly - self.sensor_positions[1]) * (ly - self.sensor_positions[1]))
                distance_right = math.sqrt((lx - self.sensor_positions[2]) * (lx - self.sensor_positions[2]) +
                                           (ly - self.sensor_positions[3]) * (ly - self.sensor_positions[3]))
                signal.append(200000 / (distance_left * distance_left))
                signal.append(200000 / (distance_right * distance_right))
        return signal

    def distance_to(self, obj):
        xx, yy = obj.get_location()
        return math.sqrt(math.pow(self.x - xx, 2) + math.pow(self.y - yy, 2))

    def collect_dirt(self, canvas, registry_passives, count):
        to_delete = []
        for idx, rr in enumerate(registry_passives):
            if isinstance(rr, Dirt):
                if self.distance_to(rr) < 30:
                    canvas.delete(rr.name)
                    to_delete.append(idx)
                    count.item_collected(canvas)
        for ii in sorted(to_delete, reverse=True):
            del registry_passives[ii]
        return registry_passives

    def transfer_function(self, charger_left, charger_right):
        # wandering behaviour
        if self.is_turning:
            self.velocity_left = -2.0
            self.velocity_right = 2.0
            self.turning_time -= 1
        else:
            self.velocity_left = 5.0
            self.velocity_right = 5.0
            self.moving_time -= 1
        if self.moving_time == 0 and not self.is_turning:
            self.turning_time = random.randrange(20, 40)
            self.is_turning = True
        if self.turning_time == 0 and self.is_turning:
            self.moving_time = random.randrange(50, 100)
            self.is_turning = False
        # battery - these are later so they have priority
        if self.battery < 600:
            if charger_right > charger_left:
                self.velocity_left = 2.0
                self.velocity_right = -2.0
            elif charger_right < charger_left:
                self.velocity_left = -2.0
                self.velocity_right = 2.0
            if abs(charger_right - charger_left) < charger_left * 0.1:  # approximately the same
                self.velocity_left = 5.0
                self.velocity_right = 5.0
            # self.vl = 5*math.sqrt(chargerR)
            # self.vr = 5*math.sqrt(chargerL)
        if charger_left + charger_right > 200 and self.battery < 1000:
            self.velocity_left = 0.0
            self.velocity_right = 0.0

    def collision(self, registry_actives):
        collision = False
        for rr in registry_actives:
            if isinstance(rr, Cat):
                if self.distance_to(rr) < 50.0:
                    # playsound("cat_sound.mp3", block=False)
                    collision = True
                    rr.jump()
        return collision