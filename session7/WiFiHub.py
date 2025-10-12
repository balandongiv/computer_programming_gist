# You need to transfer the WiFiHub class and the way of calling the class to the main function, into the session7_passive_component_template

class WiFiHub(Charger):
    def __init__(self, canvas, object_name, xp, yp):
        # You need to transfer the init content as we discuss in the intro section of activity 4
        super().__init__(canvas, object_name, object_size=10) # Call Charger's constructor with object_size=10 for WiFiHub
        self.centreX = xp
        self.centreY = yp


    def draw(self):
        # You need to transfer the draw content as we discuss in the intro section of activity 4
        body = self.canvas.create_oval(self.centreX - self.object_size, self.centreY - self.object_size, # Use self.object_size here
                                       self.centreX + self.object_size, self.centreY + self.object_size, # Use self.object_size here
                                       fill="purple", tags=self.name)
        return body


def main():


    wifi_1 = WiFiHub(canvas, "WifiHub", 950, 50)
    wifi_1.draw()
    print(f"Location of {wifi_1.name}: {wifi_1.get_location()}") # Added print location for WiFiHub
