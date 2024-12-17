# we have two ways to import modules
# 1. import module_name
# 2. from module_name import function_name
from sales import calc_shipping, calc_tax
import sales

sales.calc_shipping()
sales.calc_tax

calc_tax()
calc_shipping()  # this will call the function from the sales module

# 1. How Python Code Works:

# Python is an interpreted language. This means that Python code is not directly executed by the computer’s hardware but instead is processed step-by-step by a program called the Python interpreter.

# When you write Python code in a .py file, Python doesn't run it directly. Instead, it goes through two steps:

#     Compilation: Your Python code is converted into an intermediate form called bytecode.
#     Execution: The bytecode is then executed by the Python interpreter.

# 2. What Are Python Compiled Files?

# The compiled Python files are the bytecode version of your code. These files are saved with the .pyc extension and are stored inside a folder called __pycache__.

# For example:

#     If you have a Python file named example.py, Python will create a compiled file called example.cpython-xx.pyc in a folder named __pycache__.

# Here:

#     cpython refers to the type of Python interpreter.
#     xx represents the version of Python (e.g., 39 for Python 3.9).

# 3. Why Does Python Use Compiled Files?

# Python uses compiled files (.pyc) to speed up execution:

#     Faster Loading: Instead of compiling the .py file to bytecode every time, Python loads the bytecode from the .pyc file, which is faster.
#     This is helpful when your code doesn’t change often.

# 4. How Does Python Know the Compiled File Is Up-To-Date?

# Python checks two things to ensure the .pyc file is up-to-date:

#     Timestamp: Python compares the last modified time of the original .py file with the compiled .pyc file.
#         If the .py file is newer, Python knows the .pyc is outdated and recompiles the code.
#     Python Version: The compiled file is version-specific (e.g., cpython-39 for Python 3.9). If you use a different version of Python, it will ignore the old .pyc file and generate a new one.

# 5. Example in Action:

#     You write example.py:

# print("Hello, World!")

# When you run it with Python:

#     python example.py

#     Python creates a folder __pycache__/ and a file like example.cpython-39.pyc.

# If you modify the original example.py file, Python detects the change (via the timestamp) and regenerates the example.cpython-39.pyc file.
# Summary for a Layman:

#     Python takes your code, converts it into a quick-to-read format called bytecode (stored in .pyc files), and runs that.
#     These .pyc files save time because Python doesn’t need to recompile code every time it runs.
#     Python checks the last modified time of your code to decide if the .pyc file is still valid or if it needs to update it.

# You can think of .pyc files like "cached" versions of your code: they help speed things up but are automatically refreshed when needed.

