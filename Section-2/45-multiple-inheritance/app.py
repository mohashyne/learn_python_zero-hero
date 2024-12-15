class Employee:
    def greet(self):
        print("Employee greet")

class Person:
    def greet(self):
        print("Person greet")
        

class Manager(Employee, Person):
    pass


manager = Manager()
# which greet method will be called?
# the greet method of the Employee class will be called, 
# because the Employee class is the first class in the Manager class inheritance list
# the python interpreter will look for the greet method in the Employee class first
# if the greet method is not found in the Employee class, 
# the python interpreter will look for the greet method in the Person class
manager.greet() # Employee greet  

#if we change the order of the inheritance list? the output will change
#  what is the implication in real life projects?


# A class can inherit from two simple classes and abstract class
# this is a good example of multiple inheritance
class Flyer:
    def fly(self):
        print("fly")
        
class Swimmer:
    def swim(self):
        print("swimming")
        
class FlyingFish(Flyer, Swimmer):
    pass                       
        
        
jellyfish = FlyingFish()
jellyfish.fly() # fly
jellyfish.swim() # swimming
print(dir(jellyfish))       