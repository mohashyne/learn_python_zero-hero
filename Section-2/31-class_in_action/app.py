class Point:
    def draw(self):
        print("draw")


p1 = Point()
p1.draw()
print(type(p1)) # <class '__main__.Point'>

p2 = Point()
print(isinstance(p2, Point)) # True
print(isinstance(p2, int)) # False


