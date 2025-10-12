import math
import random

import numpy as np

from passive_component import Dirt, Charger

# Task 3
class RobotAgent:
    def __init__(self, robot_obj):
        self.is_turning = robot_obj.is_turning
        self.axle_length = robot_obj.axle_length
        self.moving = robot_obj.moving
        self.name = robot_obj.name
        self.sensor_positions = robot_obj.sensor_positions
        self.theta = robot_obj.theta
        self.turning = robot_obj.turning
        self.left_velocity = robot_obj.left_velocity
        self.right_velocity = robot_obj.right_velocity
        self.x = robot_obj.x
        self.y = robot_obj.y
        self.battery = robot_obj.battery
        self.draw = robot_obj.draw
        self.canvas = robot_obj.canvas

    # cf. Dudek and Jenkin, Computational Principles of Mobile Robotics
    def move(self, canvas, registry_passives, dt):
        if self.battery > 0:
            self.battery -= 1
        if self.battery == 0:
            self.left_velocity = 0
            self.right_velocity = 0

        for rr in registry_passives:
            if isinstance(rr, Charger) and self.distance_to(rr) < 80:
                self.battery += 10

        if self.left_velocity == self.right_velocity:
            R = 0
        else:
            R = (self.axle_length / 2.0) * ((self.right_velocity + self.left_velocity) / (self.left_velocity - self.right_velocity))

        omega = (self.left_velocity - self.right_velocity) / self.axle_length
        ICCx = self.x - R * math.sin(self.theta)  # instantaneous center of curvature
        ICCy = self.y + R * math.cos(self.theta)
        m = np.matrix([[math.cos(omega * dt), -math.sin(omega * dt), 0],
                       [math.sin(omega * dt), math.cos(omega * dt), 0],
                       [0, 0, 1]])
        v1 = np.matrix([[self.x - ICCx], [self.y - ICCy], [self.theta]])
        v2 = np.matrix([[ICCx], [ICCy], [omega * dt]])
        newv = np.add(np.dot(m, v1), v2)
        newX = newv.item(0)
        newY = newv.item(1)
        newTheta = newv.item(2)
        newTheta = newTheta % (2.0 * math.pi)  # make sure angle doesn't go outside [0.0,2*pi)
        self.x = newX
        self.y = newY
        self.theta = newTheta
        if self.left_velocity == self.right_velocity:  #  Straight line movement
            self.x += self.right_velocity * math.cos(self.theta)  # vr wlog,
            self.y += self.right_velocity * math.sin(self.theta)
        if self.x < 0.0:
            self.x = 999.0
        if self.x > 1000.0:
            self.x = 0.0
        if self.y < 0.0:
            self.y = 999.0
        if self.y > 1000.0:
            self.y = 0.0

        canvas.delete(self.name)
        self.draw(canvas)

    def pick_up_and_put_down(self, x, y):
        self.x = x
        self.y = y
        self.canvas.delete(self.name)
        self.draw(self.canvas)

    def sense_charger(self, registry_passives):
        light_l = 0.0
        light_r = 0.0
        for pp in registry_passives:
            if isinstance(pp, Charger):
                lx, ly = pp.get_location()  # Renamed function for PEP 8
                distanceL = math.sqrt((lx - self.sensor_positions[0]) * (lx - self.sensor_positions[0]) +
                                      (ly - self.sensor_positions[1]) * (ly - self.sensor_positions[1]))
                distanceR = math.sqrt((lx - self.sensor_positions[2]) * (lx - self.sensor_positions[2]) +
                                      (ly - self.sensor_positions[3]) * (ly - self.sensor_positions[3]))
                light_l += 200000 / (distanceL * distanceL)
                light_r += 200000 / (distanceR * distanceR)
        return light_l, light_r


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


    def transfer_function(self, charger_l, charger_r):
        # wandering behavior
        if self.is_turning:
            self.left_velocity = -2.0
            self.right_velocity = 2.0
            self.turning -= 1
        else:
            self.left_velocity = 5.0
            self.right_velocity = 5.0
            self.moving -= 1
        if self.moving == 0 and not self.is_turning:
            self.turning = random.randrange(20, 40)
            self.is_turning = True
        if self.turning == 0 and self.is_turning:
            self.moving = random.randrange(50, 100)
            self.is_turning = False

        # battery - these are later so they have priority
        if self.battery < 600:
            self.left_velocity = 5 * math.sqrt(charger_r)
            self.right_velocity = 5 * math.sqrt(charger_l)
        if charger_l + charger_r > 200 and self.battery < 1000:
            self.left_velocity = 0.0
            self.right_velocity = 0.0