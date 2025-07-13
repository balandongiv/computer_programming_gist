import random
import sys
import tkinter as tk

from active_component import Bot
from counter import Counter
from passive_component import Charger, WiFiHub, Dirt
from cat import Cat

# Constants
NO_OF_BOTS = 4
NO_OF_CATS = 100
NO_OF_DIRT = 300
NUMBER_OF_MOVES = 100000
TRAINING_LOOPS = 10
TRAINING_SAMPLES = 100


def button_clicked(x, y, registry_actives):
    """Move bot to the clicked position."""
    for obj in registry_actives:
        if isinstance(obj, Bot):
            obj.x = x
            obj.y = y


def initialise(window):
    """Initialise the GUI window and canvas."""
    window.resizable(False, False)
    canvas = tk.Canvas(window, width=1000, height=1000)
    canvas.pack()
    return canvas


def register(canvas):
    """Register all active and passive components."""
    registry_actives = []
    registry_passives = []

    for i in range(NO_OF_BOTS):
        bot = Bot(f"Bot{i}", canvas)
        registry_actives.append(bot)
        bot.draw(canvas)

    for i in range(NO_OF_CATS):
        cat = Cat(f"Cat{i}", canvas)
        registry_actives.append(cat)
        cat.draw(canvas)

    charger = Charger("Charger")
    registry_passives.append(charger)
    charger.draw(canvas)

    hubs = [
        WiFiHub("Hub1", 950, 50),
        WiFiHub("Hub2", 50, 500),
        WiFiHub("Hub3", 600, 800),
    ]
    for hub in hubs:
        registry_passives.append(hub)
        hub.draw(canvas)

    for i in range(NO_OF_DIRT):
        dirt = Dirt(f"Dirt{i}")
        registry_passives.append(dirt)
        dirt.draw(canvas)

    count = Counter(canvas)

    canvas.bind("<Button-1>", lambda event: button_clicked(event.x, event.y, registry_actives))

    return registry_actives, registry_passives, count


def move_it(canvas, registry_actives, registry_passives, count, moves, signal_strengths):
    """Main movement loop for bots and cats."""
    moves += 1

    for obj in registry_actives:
        if isinstance(obj, Bot):
            obj.look(registry_actives)
            intensity_l, intensity_r = obj.sense_charger(registry_passives)
            obj.transfer_function(intensity_l, intensity_r)

        if isinstance(obj, Cat):
            obj.transfer_function()

        obj.move(canvas, registry_passives, 1.0)

        if isinstance(obj, Bot):
            registry_passives = obj.collect_dirt(canvas, registry_passives, count)
            _ = obj.collision(registry_actives)

    if moves > NUMBER_OF_MOVES:
        print(f"Total dirt collected in {NUMBER_OF_MOVES} moves is {count.dirt_collected}")
        sys.exit()

    canvas.after(50, move_it, canvas, registry_actives, registry_passives, count, moves, signal_strengths)


def training(registry_actives, registry_passives, canvas):
    """Training phase to collect signal strengths from hub sensing."""
    bot = registry_actives[0]
    signal_strengths = []

    for x in range(TRAINING_LOOPS):
        for y in range(TRAINING_LOOPS):
            top_corner_x = x * 100.0
            top_corner_y = y * 100.0

            for _ in range(TRAINING_SAMPLES):
                pos_x = top_corner_x + random.uniform(0.0, 100.0)
                pos_y = top_corner_y + random.uniform(0.0, 100.0)
                bot.pick_up_and_put_down(pos_x, pos_y)
                signal_strengths.append((bot.sense_hubs(registry_passives), x, y))

    return signal_strengths


def main():
    window = tk.Tk()
    canvas = initialise(window)
    registry_actives, registry_passives, count = register(canvas)
    signal_strengths = training(registry_actives, registry_passives, canvas)
    moves = 0
    move_it(canvas, registry_actives, registry_passives, count, moves, signal_strengths)
    window.mainloop()


if __name__ == "__main__":
    main()
