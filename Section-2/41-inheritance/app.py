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


mammal = Mammal()
mammal.eat() # eat
mammal.walk() # walk

fish = Fish()
fish.eat() # eat
fish.walk() # swim
print(fish.age) # 1
