class Point:
    default_color = "red"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other) :
        return self.x == other.x and self.y == other.y and self.z == other.z  

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z
    
    # if you implement the __gt__ method, python will automatically implement the __lt__ method
        

      

point_one = Point(1, 2, 3)
point_two = Point(1, 2, 3)
#  



# by default, the equality operator compares the memory address of two objects
# to compare the values of two objects, you need to override the __eq__ method
# the __eq__ method is a magic method that is called when you use the equality operator

# after the __eq__ method is implemented, the equality operator will compare the values of two objects
# instead of comparing the memory address of two objects
# the __eq__ method should return a boolean value
# the __eq__ method takes two arguments: self and other
# self is the current object
# other is the object that you are comparing to
# you can compare the values of two objects using the self and other objects

print(point_one == point_two) # True
