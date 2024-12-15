class Animal:
    def eat(self):
        print("eat")
        
class Bird(Animal):
    def fly(self):
        print("fly")  

# Bird is the child class of Animal
# since a chicken cannot fly, we can create a chicken class that will inherit from the Bird class
# and override the fly method, so that the chicken cannot fly
# if we do that, that is a class abuse, because we are changing the behavior of the base class 
class Chicken(Bird):
    pass  # pass is used to indicate that the class is empty, it is used as a placeholder
          # we cannot leave the class empty, we need to have at least one statement in the class
          
          
# Employee - Person - LivingCreature - Thing
# Employee is a Person and a Person is a LivingCreature and a LivingCreature is a Thing
# Employee is a LivingCreature and a Thing as well 
# Employee is a multi-level inheritance
# multi-level inheritance is not recommended, because it makes the code complex
# IF you  want to use inheritance, it is better you go one or two levels deep
# it is better to use composition instead of inheritance
# class Employee(Person): # this is a single inheritance
# class Employee(Person, LivingCreature): # this is a multiple inheritance
# class Employee(LivingCreature, Person): # this is a multiple inheritance
# class Employee(Thing, LivingCreature, Person): # this is a multiple inheritance
                       