message = "a"

def greet():
    message = "b" # local , if you dont declare this it will inherit the global variable
    print(message)
    
    
greet() # b 
print(message)  # a  (global)