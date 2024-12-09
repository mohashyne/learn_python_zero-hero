class Point:
    default_color = "red"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)
        

    def draw(self):
        print(f"Point ({self.x}, {self.y}, {self.z})")

# instead of using class attributes, you can use class methods
# class methods are methods that are bound to the class, not the object
# class methods are defined with the decorator @classmethod
# class methods take cls as the first argument
# i.e this can save you from assigning tags/serial numbers to objects
p1 = Point(0, 0, 1) # manually assigning tags/serial numbers to objects
p1.draw() # Point (0, 0, 1)


# automatically assigning tags/serial numbers to objects
p2 = Point.zero() # automatically assigning tags/serial numbers to objects
p2.draw() # Point (0, 0, 0)