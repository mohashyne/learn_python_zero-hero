class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal is the base class
# Mammal and Fish are the child, sub or derived classes


class Mammal(Animal):
    # this constructor will override the constructor in the base class
    # to call the constructor in the base class we use the super() function
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


mammal = Mammal()
mammal.walk()  # walk
print(mammal.weight)  # 2
# print(mammal.age) # AttributeError: 'Mammal' object has no attribute 'age' , this is because the __init__ method in the base class is not called.

# to fix this we need to call the __init__ method of the base class in the __init__ method of the derived class
# we can do this by calling the super() function
# super() function returns the base class
# super().__init__() will call the __init__ method of the base class

print(mammal.__dict__)  # {'weight': 2} , the age attribute is not in the dictionary because the __init__ method of the base class is not called

print(dir(mammal))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'eat', 'walk', 'weight']

