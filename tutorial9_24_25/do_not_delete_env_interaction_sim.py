import sys
import tkinter as tk
import numpy as np

from active_component import Bot
from dynamic_component import RobotAgent
from passive_component import Dirt, Counter, WiFiHub, Charger
from helper.robot_helper import initialize_canvas, bot_clicked


class SimulationWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.should_stop = False
# ------------------------- REGISTRATION FUNCTION -------------------------
def register_components(canvas, num_bots, num_dirt_patches, hub_locations):
    bots = []
    passive_components = []

    # Register bots
    for i in range(num_bots):
        bot = Bot(f"Bot_{i}", canvas)
        bots.append(bot)
        bot.draw(canvas)

    # Register charger
    charger = Charger("Charger")
    passive_components.append(charger)
    charger.draw(canvas)

    # Register WiFi Hubs
    for hub_id, (x, y) in enumerate(hub_locations):
        hub = WiFiHub(f"Hub_{hub_id}", x, y)
        passive_components.append(hub)
        hub.draw(canvas)

    # Register dirt patches
    for i in range(num_dirt_patches):
        dirt = Dirt(f"Dirt_{i}")
        passive_components.append(dirt)
        dirt.draw(canvas)

    # Counter for dirt collection
    dirt_counter = Counter(canvas)

    # Enable robot repositioning on mouse click
    canvas.bind("<Button-1>", lambda event: bot_clicked(event.x, event.y, bots, Bot))

    return bots, passive_components, dirt_counter


# ------------------------- ROBOT MOVEMENT FUNCTION -------------------------
def move_robots(canvas, bots, passive_components, dirt_counter, moves, max_moves, move_delay,window):
    if window.should_stop:
        return
    moves += 1
    # print(f'Move count: {moves}')

    for bot in bots:
        agent = RobotAgent(bot)
        charger_intensity_left, charger_intensity_right = agent.sense_charger(passive_components)
        agent.transfer_function(charger_intensity_left, charger_intensity_right)
        agent.move(canvas, passive_components, dt=1.0)

        # Update bot state from agent (more efficient way)
        bot.x = agent.x
        bot.y = agent.y
        bot.theta = agent.theta
        bot.battery = agent.battery
        bot.sensor_positions = agent.sensor_positions

        # Dirt collection
        passive_components = agent.collect_dirt(canvas, passive_components, dirt_counter)

    if moves > max_moves:
        print(f"Total dirt collected after {max_moves} moves: {dirt_counter.dirt_collected}")
        # sys.exit()  # Or window.destroy() to close the window
        window.should_stop = True
        window.root.after(10,  window.root.destroy)  # Schedule window to close after this call finishes

    canvas.after(move_delay, move_robots, canvas, bots, passive_components, dirt_counter, moves, max_moves, move_delay,window)


# ------------------------- MAIN FUNCTION -------------------------
def run_simulation(NUM_BOTS=0, MAX_MOVES=0):


    NUM_DIRT_PATCHES = 300
    HUB_LOCATIONS = [(950, 50), (50, 500)]
    MOVE_DELAY_MS = 20  # Time delay between moves (in milliseconds)
    sim = SimulationWindow()
    canvas = initialize_canvas(sim.root)

    bots, passive_components, dirt_counter = register_components(
        canvas, NUM_BOTS, NUM_DIRT_PATCHES, HUB_LOCATIONS
    )

    move_robots(canvas, bots, passive_components, dirt_counter, 0, MAX_MOVES, MOVE_DELAY_MS,sim)

    sim.root.mainloop()
    return dirt_counter.dirt_collected

if __name__ == "__main__":
    opt=run_simulation(NUM_BOTS = 30,
         MAX_MOVES = 4)
    print(f'Total dirt collected: {opt}')