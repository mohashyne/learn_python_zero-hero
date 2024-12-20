from pathlib import Path
import shutil
from time import ctime


file_in_path = Path("Section-3/10-files/ecommerce/__init__.py")

# print(file_in_path.exists())
# print(file_in_path.is_file())
# print(file_in_path.rename("init.txt"))
# print(file_in_path.unlink())
# print(file_in_path.write_text("Hello, Python!"))
# print(file_in_path.read_text())

# print(file_in_path.stat())
#os.stat_result(st_mode=33188, st_ino=2256683, st_dev=29, st_nlink=1, st_uid=1000, st_gid=1003, st_size=29, st_atime=1734600001, st_mtime=1734600001, st_ctime=1734600001)


print(ctime(file_in_path.stat().st_ctime)) # Thu Dec 19 02:20:01 2024

# print(file_in_path.read_bytes)


# instead of using the with open() as file: block, you can use the read_text() method to read the contents of a file.
print(file_in_path.read_text())
print(file_in_path.read_bytes())
print(file_in_path.write_text("Hello, Python!"))


# when it comes to copying files, you can use the shutil module's copy() method. This method takes two arguments: the source file and the destination file.
source = file_in_path
target = Path() / "Section-2"

shutil.copy(source, target)

# other ways of coping files
# target.write_text(source.read_text())
