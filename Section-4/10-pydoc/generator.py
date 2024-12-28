import subprocess

def generate_pydoc(module_name, output_file):
    """
    Generate the documentation for a given Python module using pydoc
    and save it to a specified file.

    Parameters:
    - module_name (str): The name of the Python module.
    - output_file (str): The file path to save the documentation.
    """
    try:
        # Run the pydoc command and capture its output
        result = subprocess.run(
            ["python3", "-m", "pydoc", module_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        # Save the output to the specified file
        with open(output_file, "w") as file:
            file.write(result.stdout)

        print(f"Documentation for '{module_name}' saved to '{output_file}'.")

    except subprocess.CalledProcessError as e:
        print(f"Error generating documentation for '{module_name}':\n{e.stderr}")

# Generate and save documentation for the 'math' module
generate_pydoc("math", "math_documentation.txt")  # Save documentation for the 'math' module

# pydoc mspdf.pdf2image  


# Run the script to generate and save the documentation for the 'math' module to html

# pydoc3  -w math
# open math.html


# pydoc3 -p 1234  # Start the pydoc HTTP server on port 1234
# http://localhost:1234  # Open a browser and navigate to the local server
# http://localhost:1234/math  # Navigate to the documentation for the 'math' module


