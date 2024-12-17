# instead of using the abstract method to archive polymorphic system, we can archive the same without it
# However its a best practice to use the abstract method , so as to enforce designed method from the parent class

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass
    
class TextBox:
    def draw(self):
        print("Drawing a textbox")  
        
class DropDownList:
    def draw(self):
        print("Drawing a dropdownlist")
        
    
    
def draw(controls):
        for control in controls:
            control.draw()
            
            
ddl = DropDownList()
textbox = TextBox() 


draw([ddl, textbox]) # Drawing a dropdownlist, Drawing a textbox    
                                