# with statement is used to open a file and automatically close it after the block of code is executed.

try:
    with open("app.py") as file: # file = open("app.py")
        print("File opened.") 
        # if an  object supports the context manager protocol, it can be used with the with statement.
        # The context manager protocol consists of the methods __enter__() and __exit__().
        # The __enter__() method returns the resource to be managed.
        # The __exit__() method is called when the block of code is exited.
        # The __exit__() method is called even if an exception is thrown.
        # The __exit__() method is used to release resources.   
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.") 
else:
    print("No exceptions were thrown.")

