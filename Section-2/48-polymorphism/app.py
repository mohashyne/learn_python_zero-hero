from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod # This is a decorator that tells python that this method is abstract and it must be implemented in the derived class
    def draw(self):
        pass
    
class TextBox(UIControl):
    def draw(self):
        print("Drawing a textbox")  
        
class DropDownList(UIControl):
    def draw(self):
        print("Drawing a dropdownlist")
        
    
    
def draw(controls):
        for control in controls:
            control.draw()
            
            
ddl = DropDownList()
textbox = TextBox() 
print(isinstance(ddl, UIControl)) # True
print(isinstance(textbox, UIControl)) # True

draw([ddl, textbox]) # Drawing a dropdownlist, Drawing a textbox    
                                