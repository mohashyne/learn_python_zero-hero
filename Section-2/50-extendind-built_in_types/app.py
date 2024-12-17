# Extending built-in types
# ===========================

class Text(str):
    def duplicate(self):
        return f"{self} - {self}"
    
    
text = Text("Python")
print(text) # Python 
print(text.lower()) #
print(text.duplicate()) # PythonPython


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object) # append method of list , this will be called if the interpreter dose not find the first append method
    
list = TrackableList()
list.append("1") # Append called (this is the customized append)

# if it was the original append method "super" that was called
# list.append("2")
# print(list) # [1, 2] 
   
        
        
        