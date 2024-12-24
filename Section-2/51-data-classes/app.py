# We use classes to bundle data and functionalities into one unit
# but as we work on larger programs, we make come across classes that do not have any  behaviour
# they don't have any methods, they only  have data

from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # to compare them base on value passed, we need to create a magic method
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    # now when we compare the two objects below the problem is  solved
    #  however writing methods for the data classes can be  tedious
    # instead we import the "nametuple"


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # False
print(id(p1))  # 4489711568
print(id(p2))  # 4489711376
print(p1 == p2)  # True


# we create a named tuple with the name "Pointer" and two fields "x" and "
Points = namedtuple('Points', ['x', 'y'])
ps1 = Points(x=1, y=2)
ps2 = Points(x=1, y=2)

# remember this name tuples are immutable
print(p1.x)  # 1
print(p2.y)  # 2
print(p1.x)
print(p1.x)
print(ps1 == ps2)  # True
print(ps1 + ps2)  # (1, 2, 1, 2)
