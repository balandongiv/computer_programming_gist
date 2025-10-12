import random
import tkinter as tk

random.seed(0)

class Dirt:
    # All of the attributes and methods are the same as in the previous activity
    pass

## This is where you should take extra care and effort to understand
class Charger(Dirt):
    def __init__(self, canvas, object_name=None, object_size=8, body_color='red'):
        super().__init__(canvas, object_name, object_size, body_color)

    def draw(self):
        square = self.canvas.create_rectangle(self.centreX - self.object_size, self.centreY - self.object_size,
                                              self.centreX + self.object_size, self.centreY + self.object_size,
                                              fill=self.body_color, tags=self.name)
        return square


def initialise_canvas(root, width=1000, height=1000):
    # This function is the same as in the previous activity
    pass

def main():
    root = tk.Tk()
    root.title("Passive Components")
    canvas = initialise_canvas(root)

    for i in range(3):
        dirt = Dirt(canvas, object_name="Dirt" + str(i), object_size=4)
        dirt.draw()
        print(f"Location of {dirt.name}: {dirt.get_location()}")

    for i in range(3):
        charger = Charger(canvas, object_name="Charger" + str(i), object_size=10,body_color='red')
        charger.draw()
        print(f"Location of {charger.name}: {charger.get_location()}")


    root.mainloop()

if __name__ == "__main__":
    main()
