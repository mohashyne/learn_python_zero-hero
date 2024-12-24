import subprocess

# running external programs with python

# Sometimes, when using Python, you might need to run other programs or commands on your computer. This is like asking Python to open a door, run something outside, and then return the result.

# Python has a module called subprocess that makes this possible.
# How Does It Work?

# Think of subprocess as a phone. Python can use it to "call" another program or command, give it instructions, and then "listen" for a response.
# Why Would You Use This?

#     Automating Repetitive Tasks:
#         Run scripts, commands, or programs without typing them manually.
#         Example: Restarting a server or copying files.

#     Combining Tools:
#         Use Python to manage tools written in other programming languages.

#     System Administration:
#         Perform tasks like listing files, managing processes, or checking network configurations.

# All this are considered as old school way of doing things, the modern way is to use the subprocess.run() function
# subprocess.call
# subprocess.check_call   
# subprocess.check_output
# subprocess.Popen



# Simple Example
# 1. Checking the Files in a Folder

# You can run the ls (Linux/macOS) or dir (Windows) command to list files in a folder.

# Here’s how Python does it:

# if we set the capture_output to True, the output of the command will be stored in the result object
# if we set output to False, the output will be printed to the console
# if we set the text to True, the details will be displayed  if we  run stdout, the output will be in string format
# result = subprocess.run(["ls", "-l"], 
#                         capture_output=True, check=True,
#                         text=True) # Linux/macOS

try:
    result = subprocess.run(["python3", "Section-3/24-running-external_program/other.py"], 
                            capture_output=True, check=True,
                            text=True,
                            check=True) # Linux/macOS
    print(result) # CompletedProcess(args=['ls', '-l'], returncode=0)

# This are the attributes of the result object
# print(dir(result)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'args', 'check_returncode', 'returncode', 'stderr', 'stdout']

    print("args: ", result.args) # ['ls', '-l']
    print("returncode: ", result.returncode) # 0 means the command ran successfully
    print("stderr: ", result.stderr) # None means no error
    print("stdout: ", result.stdout) # total 16 means the number of files in the folder 
except subprocess.CalledProcessError as ex:
    print("Error: ", ex) # Error: CompletedProcess(args=['ls', '-l'],





# subprocess.run(["dir"], check=True)  # Windows


# 2. Pinging a Website
# You can use the ping command to check if a website is reachable:
# Run the 'ping' command
# result = subprocess.run(["ping", "-c", "3", "google.com"], capture_output=True, text=True)

# # Print the output of the command
# print("Ping Results:")
# print(result.stdout)

# Output (example):
# Ping Results:
# PING google.com (142.250.190.142): 56 data bytes
# 64 bytes from 142.250.190.142: icmp_seq=0 ttl=117 time=10.567 ms
# 64 bytes from 142.250.190.142: icmp_seq=1 ttl=117 time=11.234 ms
# 64 bytes from 142.250.190.142: icmp_seq=2 ttl=117 time=9.876 ms

# How to Handle Errors?
# If the command fails, Python will let you know:



# try:
#     # Run a non-existent command
#     result = subprocess.run(["fakecommand"], capture_output=True, text=True, check=True)
# except subprocess.CalledProcessError as e:
#     print("The command failed!")
#     print(e)

# Output:
# The command failed!
# [Errno 2] No such file or directory: 'fakecommand'

# Layman Example: Making Coffee

# Think of Python as a coffee machine and subprocess as a person who presses the buttons:

#     You tell the machine (subprocess) what kind of coffee to make (external program).
#     It makes the coffee for you and gives you the cup (output).

# In this context:

#     Coffee machine = Python
#     Button you press = Command
#     Coffee = Result/output of the external program

# With subprocess, Python becomes a multitasker, able to run other programs and use their results in your code. This is especially helpful for admins automating tasks across systems!



# try:
#     result = subprocess.run(["false"], 
#                             capture_output=True, check=True,
#                             text=True,
#                             check=True) # Linux/macOS
#     print(result) # CompletedProcess(args=['ls', '-l'], returncode=0)

# # This are the attributes of the result object
# # print(dir(result)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'args', 'check_returncode', 'returncode', 'stderr', 'stdout']

#     print("args: ", result.args) # ['ls', '-l']
#     print("returncode: ", result.returncode) # 0 means the command ran successfully
#     print("stderr: ", result.stderr) # None means no error
#     print("stdout: ", result.stdout) # total 16 means the number of files in the folder 
# except subprocess.CalledProcessError as ex:
#     print("Error: ", ex) # Error: CompletedProcess(args=['ls', '-l'],