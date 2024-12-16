class InvalidOperationError(Exception):
    pass

class Stream:
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
        
class FileStream(Stream):
    def read(self):
        print("Reading data from a file") 
             
class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network") 
             
class DatabaseStream(Stream):
    def read(self):
        print("Reading data from a Database")   
        
        
vet_db = DatabaseStream()
vet_db.read()
vet_db.open()
vet_db.open()  # Error: Stream is already opened   


# Working with a file stream
file_stream = FileStream()

file_stream.open()  # Opens the file
file_stream.read()  # Reads data from the file


# Attempting to reopen without closing:
file_stream.open()  # Error: Stream is already opened
      

            