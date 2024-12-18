from pathlib import Path

#pathlib object oriented filesystem

Path(r"C:\Program Files\Microsoft")
Path("usr/local/bin")
Path()
Path("ecommerce/__init__.py")
Path() / "ecommerce" / "__init__.py"
Path.home()

# Understanding Path Objects in Python
# Python's Path class (part of the pathlib module) helps you manage and interact with file paths more efficiently. It works across different operating systems like Windows, Linux, and macOS.

# Below is an explanation of different Path methods and examples:

# Example	What It Means	When to Use It
# Path(r"C:\Program Files\Microsoft")	- Represents a Windows file path using a raw string.	Use it when working with absolute paths on Windows, particularly when accessing a specific folder or file.

# Path("usr/local/bin")	- Represents a relative path to usr/local/bin.
# This works on Linux, macOS, or in relative directories.	Use when working with relative paths to access folders in Unix-like systems or within project directories.

# Path()	- Represents the current working directory (where the program is running).	Use it to interact with files in the current folder without hardcoding a path.

# Path("ecommerce/__init__.py")	- Points to a file named __init__.py inside the ecommerce directory.	Use it to access files within a specific folder structure, like in projects or Python packages.

# Path() / "ecommerce" / "__init__.py"	- Combines the current directory (Path()) with subdirectories (ecommerce) and a file (__init__.py).
# This is cleaner and cross-platform.	Use to build paths dynamically instead of hardcoding them. It’s useful for creating or accessing nested files.

# Path.home()	- Points to the home directory of the current user (e.g., /home/username on Linux or C:\Users\username on Windows).	Use it when you want to access user-specific files or directories, like in configuration files or personal scripts.

# Quick Definitions of Key Terms:
# Absolute Path: A full path starting from the root (e.g., C:\ on Windows, / on Linux).
# Relative Path: A path relative to the current working directory.
# Raw String (r"..."): A string where backslashes (\) are treated literally, avoiding escape character issues in Windows paths.
# Path Chaining: Using / with Path to dynamically join folders and files (platform-independent).


# Why Use Path Instead of Strings?
# Path is more readable, robust, and works across all operating systems.
# You can perform file operations like checking if a file exists, reading, or writing in a clean, intuitive way.
# This breakdown helps you understand each Path use case and when to apply them in practical scenarios. Let me know if you want examples of operations like creating or checking files!


