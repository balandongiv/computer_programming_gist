import sys
import tkinter as tk
import numpy as np

# Task 1
from helper.robot_helper import initialize_canvas, bot_clicked, SimulationWindow

# Task 3
from active_component import Bot
from passive_component import Dirt, Counter, WiFiHub, Charger

# Task 3
# from dynamic_component import RobotAgent

np.random.seed(0)

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
# Task 3: import the move_robots
def move_robots():
    pass


# ------------------------- MAIN FUNCTION -------------------------
def run_simulation():

    NUM_BOTS = 30
    NUM_DIRT_PATCHES = 300
    HUB_LOCATIONS = [(950, 50), (50, 500)]
    MAX_MOVES = 200000
    MOVE_DELAY_MS = 20  # Time delay between moves (in milliseconds)
    sim = SimulationWindow()
    canvas = initialize_canvas(sim.root)

    bots, passive_components, dirt_counter = register_components(
        canvas, NUM_BOTS, NUM_DIRT_PATCHES, HUB_LOCATIONS
    )

    # Task 3
    move_robots(canvas, bots, passive_components, dirt_counter, 0, MAX_MOVES, MOVE_DELAY_MS,sim)

    sim.root.mainloop()


if __name__ == "__main__":
    run_simulation()