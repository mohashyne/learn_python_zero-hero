class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def draw(self):
        print(f"Point ({self.x}, {self.y})")

# class level attribute is shared by all instances of a class
Point.default_color = "yellow" # class level attribute

p1 = Point(1, 2)
print(p1.x)
print(p1.default_color) # red
print(Point.default_color) # red

# difference between class and instance attributes
p1.default_color = "blue" # instance level attribute
print(p1.default_color) # blue
print(Point.default_color) # red

p1.draw()

# in real world applications, you will be using instance attributes more than class attributes
# because you will be working with objects more than classes
# class attributes are used to store data that is shared by all instances of a class
# instance attributes are used to store data that is unique to each instance of a class
# class attributes are defined outside the constructor
# instance attributes are defined inside the constructor