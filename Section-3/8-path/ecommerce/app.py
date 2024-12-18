from pathlib import Path

path = Path("ecommerce/__init__.py")
(path.exists()) # True
(path.is_file())
(path.is_dir())
print(path.name) # __init__.py
print(path.stem) # __init__
print(path.suffix) # .py
print(path.parent) # ecommerce
# path = path.with_name("file.txt") # ecommerce/file.txt
# print(path) # ecommerce/file.txt
path = path.with_suffix(".txt") # ecommerce/__init__.txt
print(path) # ecommerce/file.txt
print(path.absolute()) # /home/username/ecommerce/file.txt
