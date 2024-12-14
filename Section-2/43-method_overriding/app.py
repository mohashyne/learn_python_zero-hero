class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")
        
    def drive(self):
        print("Driving")
        
    def brake(self):
        print("Braking")
        
        
class Honda(Car):
    def drive(self):
        print("I am driving a toyota")
        
        
lastest_model = Honda("Civic", "Coupe", "1999")
lastest_model.drive      
            
        