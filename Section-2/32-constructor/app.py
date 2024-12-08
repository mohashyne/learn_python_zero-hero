class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        print(f"Point ({self.x}, {self.y})")


p1 = Point(1, 2)
print(p1.x)

p1.draw()

# A constructor is a special method in Python that gets called when an object is created.
# The constructor method is called __init__ (two underscores before and after init)
# The constructor method is also called initializer
# The constructor method is also called dunder init
# The constructor method is also called magic method
# the diffence of class and contructor in ruby and python is that in python the 
# constructor is a method that is called when an object is created,
# while in ruby the constructor is a method that is called when a class is created


