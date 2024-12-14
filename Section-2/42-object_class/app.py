# Object is the base calss for all classes in Python. All classes in Python inherit from the Object class.

class Animal:
     def __init__(self):
        self.age = 1

     def eat(self):
        print("eat")

# Animal is the base class
# Mammal and Fish are the child, sub or derived classes
class Mammal(Animal):  
    def walk(self):
        print("walk")    

class Fish(Animal):
    def walk(self):
        print("swim")            


print(issubclass(Animal, object)) # True

m = Mammal()
m.eat() # eat
m.walk() # walk
print(isinstance(m, Animal)) # True
print(isinstance(m, object)) # True
print(issubclass(Mammal, Animal)) # True
print(issubclass(Mammal, object)) # True

f = Fish()
f.eat() # eat
f.walk() # swim
print(f.age) # 1
print(isinstance(f, Animal)) # True
print(isinstance(f, object)) # True
print(issubclass(Fish, Animal)) # True
print(issubclass(Fish, object)) # True
print(issubclass(Animal, Mammal)) # False

# o will inherit all the methods and attributes of the object class 
# i.e the __init__ method, __str__ method, __eq__ method, __hash__ method,
# __repr__ method, __del__ method, __new__ method, __reduce__ method,
# __reduce_ex__ method, __getattribute__ method, __setattr__ method, 
# __delattr__ method, __dir__ method, __class__ method, __doc__ method,
# __sizeof__ method, __subclasshook__ method, __init_subclass__ method,
# from parent or child classes of the object class
o = object()
print(isinstance(o, object)) # True
