import random

class Dirt:
    def __init__(self, name):
        self.center_x = random.randint(100, 900)
        self.center_y = random.randint(100, 900)
        self.name = name

    def draw(self, canvas):
        dirt_constant = 4
        canvas.create_oval(self.center_x - dirt_constant, self.center_y - dirt_constant,
                           self.center_x + dirt_constant, self.center_y + dirt_constant,
                           fill="grey", tags=self.name)

    def get_location(self):
        return self.center_x, self.center_y


class Counter:
    def __init__(self, canvas):
        self.dirt_collected = 0
        self.canvas = canvas
        self.canvas.create_text(70, 50, text="Dirt collected: " + str(self.dirt_collected), tags="counter")

    def item_collected(self, canvas):
        self.dirt_collected += 1
        self.canvas.itemconfigure("counter", text="Dirt collected: " + str(self.dirt_collected))


class Charger:
    def __init__(self, name):
        self.center_x = random.randint(100, 900)
        self.center_y = random.randint(100, 900)
        self.name = name

    def draw(self, canvas):
        canvas.create_oval(self.center_x - 10, self.center_y - 10,
                           self.center_x + 10, self.center_y + 10,
                           fill="gold", tags=self.name)

    def get_location(self):
        return self.center_x, self.center_y


class WiFiHub:
    def __init__(self, name, x, y):
        self.center_x = x
        self.center_y = y
        self.name = name

    def draw(self, canvas):
        canvas.create_oval(self.center_x - 10, self.center_y - 10,
                           self.center_x + 10, self.center_y + 10,
                           fill="purple", tags=self.name)

    def get_location(self):
        return self.center_x, self.center_y