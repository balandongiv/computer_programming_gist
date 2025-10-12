class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    ## How to add methods to the class ##
    # def distance_from_origin(self):
    #     x_sq = self.x ** 2
    #     y_sq = self.y ** 2
    #     distance = (x_sq + y_sq) ** 0.5
    #     return distance

    ## Modify the __str__ method to print the object in a readable format ##
    # def __str__(self):
    #     return f"<The x Val: {self.x} and the y Val: {self.y}>"


# c = Coordinate(3,4)
# Accessing the class attribute using dot notation
# print(c.x)

# Creating another object of the class
# Origin = Coordinate(0,0)


## How to use procedural method
# dist_val=c.distance_from_origin()
# print("Distance from origin:",dist_val)

## Another approach to use the class
# dist_val_another_approach=Coordinate.distance_from_origin(c)

## Modify the __str__ method to print the object in a readable format ##
# point = Coordinate(3, 4)
# print (point)


im_here_so_that_we_can_see_the_output = c.x