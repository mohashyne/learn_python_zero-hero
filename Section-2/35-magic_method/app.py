# magic methods start and end with __
# magic methods are called by the python interpreter
# magic methods are used to implement operator overloading
# magic methods are also called dunder methods

# https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#special-method-names

class Point:
    default_color = "red"

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"    

    @classmethod # class method decorator  
    def zero(cls): # cls is the class itself
        return cls(0, 0, 0) # cls is used to create an instance of the class itself , if the user dose not provide any values for the class attributes, the class attributes will be set to 0   

    def draw(self):
        print(f"Point ({self.x}, {self.y}, {self.z})")

      

p1 = Point(0, 0, 1) # manually assigning tags/serial numbers to objects
print(p1)

# key magic methods includes:
# __init__ : constructor
# __str__ : string representation
# __eq__ : equality
# __lt__ : less than
# __gt__ : greater than
# __le__ : less than or equal to
# __ge__ : greater than or equal to
# __ne__ : not equal to
# __add__ : addition
# __sub__ : subtraction
# __mul__ : multiplication
# __truediv__ : division
# __floordiv__ : floor division
# __mod__ : modulus
# __pow__ : exponentiation
# __len__ : length
# __getitem__ : indexing
# __setitem__ : setting values
# __delitem__ : deleting values
# __iter__ : iteration
# __contains__ : containment check
# __call__ : make the instance callable
# __enter__ : context manager entry
# __exit__ : context manager exit
# __new__ : create a new instance
# __getattr__ : get attribute
# __setattr__ : set attribute
# __delattr__ : delete attribute
# __dir__ : directory listing
# __doc__ : access docstring
# __hash__ : hash values
# __repr__ : debugging and logging
# __copy__ : shallow copy
# __deepcopy__ : deep copy
# __format__ : custom string formatting
# __reduce__ : pickling
# __reduce_ex__ : pickling
# __instancecheck__ : isinstance()
# __subclasscheck__ : issubclass()
# __trunc__ : trunc()
# __floor__ : math.floor()
# __ceil__ : math.ceil()
# __round__ : round()
# __get__ : descriptor protocol
# __set__ : descriptor protocol
# __delete__ : descriptor protocol
# __set_name__ : descriptor protocol
# __class_getitem__ : class method
# __class__ : class method
# __prepare__ : metaclass method
# __init_subclass__ : metaclass method
# __subclasshook__ : metaclass method
# __import__ : import hooks
# __loader__ : import hooks
# __package__ : import hooks
# __spec__ : import hooks
# __annotations__ : type hints
# __builtins__ : built-in scope