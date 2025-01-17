# Using pydoc on Mac and Windows

# pydoc is a Python module that generates and displays documentation for Python modules, classes, functions, and methods.
# 1. On Mac
# View Documentation in the Terminal

#     Open the Terminal.
#     Run pydoc with the target module, class, or function:

# python3 -m pydoc module_name

# Example:

#     python3 -m pydoc math

# Generate and View Documentation in a Web Browser

#     Start the pydoc HTTP server:

# python3 -m pydoc -p 1234

#     This starts a documentation server on port 1234.

# Open a browser and navigate to:

#     http://localhost:1234

# Save Documentation to a Text File

#     Redirect the output of pydoc to a file:

#     python3 -m pydoc module_name > output.txt

# 2. On Windows
# View Documentation in the Command Prompt

#     Open Command Prompt (or PowerShell).
#     Use the python command with pydoc:

# python -m pydoc module_name

# Example:

#     python -m pydoc os

# Generate and View Documentation in a Web Browser

#     Start the pydoc HTTP server:

# python -m pydoc -p 1234

#     Open a browser and navigate to:

#     http://localhost:1234

# Save Documentation to a Text File

#     Redirect the output to a file:

#     python -m pydoc module_name > output.txt

# Additional Tips

#     Search for Documentation of Installed Modules:

# python3 -m pydoc -k keyword

# This searches for modules, classes, or functions related to the keyword.

# View Specific Attributes:

# python3 -m pydoc module_name.attribute

# Access Help Without Command Line:

#     Use help() in the Python interactive shell:

#         >>> help(module_name)

# Troubleshooting

#     Ensure Python is installed and added to your PATH on both Mac and Windows.
#     If pydoc fails, ensure you’re using the correct version of Python:

# python3 -m ensurepip --upgrade

# python3 -m pydoc math   