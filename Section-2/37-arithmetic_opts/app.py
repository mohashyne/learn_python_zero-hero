class Point:
    default_color = "red"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other) :
        return Point(self.x + other.x, self.y + other.y, self.z + other.z) 

    def __sub__(self, other) :
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)
    
    # if you implement the __gt__ method, python will automatically implement the __lt__ method
        

      

point_one = Point(10, 2, 3)
point_two = Point(1, 2, 3)

combined = point_one + point_two 
print(combined.x) # 11
print(combined.y) # 4
print(combined.z) # 6
print(combined) # <__main__.Point object at 0x7fc1bf6a96d0>

difference = point_one - point_two
print(difference.x) # 9
print(difference) # <__main__.Point object at 0x7f8b3c7b3b50>


