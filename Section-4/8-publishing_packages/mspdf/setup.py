import setuptools
from pathlib import Path

# Ensure the README file exists before reading
readme_file = Path("README.md")
if not readme_file.is_file():
    raise FileNotFoundError("README.md file not found. Please ensure it exists in the project directory.")

setuptools.setup(
    name="mspdf",
    version="1.0",
    description="A PDF management tool",  # Add a short description
    long_description=readme_file.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",  # Specify markdown if applicable
    packages=setuptools.find_packages(exclude=["test", "data"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify minimum Python version
)

# TODO: configure virtual environment: