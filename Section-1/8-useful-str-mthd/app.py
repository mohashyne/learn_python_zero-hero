course = "  Python Programming "

print(course.upper()) # PYTHON PROGRAMMING
print(course.lower()) # python programming
print(course.title()) # Python Programming
print(course.strip()) # it strips white spaces


# finding index of character
print(course.find("Pro")) # string comparisons are case sensitive
print(course.replace(" ", "-")) #  -ython -rogramming

print("Programming" in course) # True
print("Programming" not in course) # False