# type annotation
age: int = 20
age = "Python"

print(age)  # Python


new_age: int = 20
new_age = "cpython"

print(new_age)

# if you set type as "int" but pass in a diff type i.e string "20", mypy will throw an error
