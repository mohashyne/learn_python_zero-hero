from pathlib import Path

path = Path("Section-3/9-directories/ecommerce")

print(path.iterdir()) # <generator object Path.iterdir at 0x7fadf70065e0>
# when we print this it gives us a generator object: 
# a generator object returns a new value anytime we iterate over it
# when we are working with a large data instead of storing each item in
# the memory, we use a generator object.

# for p in path.iterdir():
#     print(p)

paths = [p for p in path.iterdir()]
print(paths) # [PosixPath('Section-3/9-directories/ecommerce/__init__.py'), PosixPath('Section-3/9-directories/ecommerce/__pycache__'), PosixPath('Section-3/9-directories/ecommerce/app.py'), PosixPath('Section-3/9-directories/ecommerce/customer'), PosixPath('Section-3/9-directories/ecommerce/shopping')]

# so now we want to filter for only directories
dir_paths = [dp for dp in path.iterdir() if dp.is_dir()]
print("MY DIRECTORIES:", dir_paths)
# MY DIRECTORIES [PosixPath('Section-3/9-directories/ecommerce/__pycache__'), PosixPath('Section-3/9-directories/ecommerce/customer'), PosixPath('Section-3/9-directories/ecommerce/shopping')]

# we have two issues with this type of seraach using iterdir:
# 1. it is not recursive
# 2. it is not very readable and maintainable / cannot search using patterns

# to solve this issue we use the glob or rglob method
glob_paths = path.glob("*.py")
print("GLOB PATHS:", [gp for gp in glob_paths])
# GLOB PATHS: [PosixPath('Section-3/9-directories/ecommerce/__init__.py'), PosixPath('Section-3/9-directories/ecommerce/app.py')]

# glob_paths_2 = path.glob("**/*.py") # ** means search in all directories
      # OR
rglob_paths = path.rglob("*.py")
print("RGLOB PATHS:", [rgp for rgp in rglob_paths])
# RGLOB PATHS: [PosixPath('Section-3/9-directories/ecommerce/__init__.py'), PosixPath('Section-3/9-directories/ecommerce/app.py'), PosixPath('Section-3/9-directories/ecommerce/customer/__init__.py'), PosixPath('Section-3/9-directories/ecommerce/customer/contact.py'), PosixPath('Section-3/9-directories/ecommerce/customer/db.py'), PosixPath('Section-3/9-directories/ecommerce/shopping/__init__.py'), PosixPath('Section-3/9-directories/ecommerce/shopping/sales.py')]

