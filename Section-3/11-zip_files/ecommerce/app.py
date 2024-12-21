from pathlib import Path
from zipfile import ZipFile

# zip = ZipFile("Section-3/11-zip_files/all_files.zip", "w")
with ZipFile("Section-3/11-zip_files/all_files.zip", "w") as zip:
    for path in Path("Section-3/11-zip_files").rglob("*/*"):
        # if path.name == "__init__.py":
           zip.write(path)
# zip.close()
  

# Purpose:
# This code takes all the files and folders inside the Section-3/11-zip_files directory and compresses them into a single ZIP file called files.zip.
# Explanation of Each Line:

#     from pathlib import Path:
#     This imports the Path class, which helps us work with file and folder paths easily. It makes it simpler to locate and list files in directories.

#     from zipfile import ZipFile:
#     This imports the ZipFile class, which allows us to create, read, and modify ZIP files.

#     with ZipFile("Section-3/11-zip_files/all_files.zip", "w") as zip::
#         This line opens a new ZIP file called all_files.zip in write mode ("w").
#         The with statement ensures that the ZIP file is properly closed after all the files are added, even if something goes wrong during the process.

#     for path in Path("Section-3/11-zip_files").rglob("*/*")::
#         Path("Section-3/11-zip_files") points to the folder you want to zip.
#         .rglob("*/*") searches for all files and folders within that folder, including subfolders.
#         The for loop goes through each file and folder found in this directory.

#     zip.write(path):
#         This line adds the current file or folder (path) to the all_files.zip archive.

#     # zip.close():
#         This line is commented out because the with statement automatically closes the ZIP file when done. You don’t need to close it manually.

# What Happens:

#     The code looks inside the Section-3/11-zip_files folder.
#     It collects all files and folders (including subfolders).
#     It compresses all of them into a ZIP file named all_files.zip.

# Why Use This:

#     To save space by compressing files.
#     To group multiple files/folders into one, making it easier to share or store them.

# Think of this like packing multiple items into a single suitcase (ZIP file) for easy handling!
