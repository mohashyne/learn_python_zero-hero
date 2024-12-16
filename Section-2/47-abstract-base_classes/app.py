from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
        
    def  open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True
        
    def close(self):
        if not self.closed:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False
    
    @abstractmethod    
    def read(self):
        pass    
        
class FileStream(Stream):
    def read(self):
        print("Reading data from a file") 
             
class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network") 
             
class DatabaseStream(Stream):
    def read(self):
        print("Reading data from a Database")
        
# after mak the Stream class an abstract class, if we try to create a child class without implementing the abstract method, we will get an error
class MemoryStream(Stream):
    pass

mem_stream = MemoryStream()  # TypeError: Can't instantiate abstract class MemoryStream with abstract method read
# to solve the issue, we need to implement the read method in the MemoryStream class.
        
#if we try to create the  stream instance without implementing the abstract method, we will be able to create the instance, but it will make no sense.
# so to solve the issue, we can use the abc module to make the Stream class an abstract class
# an abstract class is a class that cannot be instantiated

      
# if we try to create an instance of Stream, we will get an error   
# This is an abstract class, it cannot be instantiated        
stream = Stream()  # TypeError: Can't instantiate abstract class Stream with abstract method read
stream.open()
stream.open()           