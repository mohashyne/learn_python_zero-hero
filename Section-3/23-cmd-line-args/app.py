import sys


# print(sys.argv)  # prints the list of command line arguments
# # ['/Users/muhammadibnsalyhu/Desktop/CODING/learn_python/Section-3/23-cmd-line-args/app.py']
# # the list must always have at least one element which is the name of the script

if len(sys.argv) == 1:
    print("USAGE: python app.py <password>")
else:
    password = sys.argv[1]
    print(f"Password: {password}")
    
    # run this script with the following command
    # python3 /Users/muhammadibnsalyhu/Desktop/CODING/learn_python/Section-3/23-cmd-line-args/app.py 123    
    # Password: 123
    
    
    
#     What Does This Code Do?

#     import sys:
#         Python has a built-in "toolbox" called sys that helps the script interact with the system.
#         One of the things it does is read arguments that you type when running the program.

#     What are sys.argv?:
#         sys.argv is a list that holds everything you type after the program name.
#         For example:
#             If you type: python app.py 1234
#             sys.argv will be: ['app.py', '1234']
#                 app.py is the program's name.
#                 1234 is the argument you passed in.

#     How Does the Script Work?:
#         It checks how many arguments you passed using len(sys.argv).
#         If you didn't type anything after the program name, it shows:

#     USAGE: python app.py <password>

#     This tells you how to use the program.
#     If you did type something (like a password), it reads the second item in the list (your input) and displays it.

# Example Usage:

#     If you run:

# python app.py 1234

# The output will be:

# Password: 1234