from timeit import timeit

code1 = """\
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """\
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code3 = """\
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor is None:
    pass
"""

# Measure execution time of each code block
print("First code:", timeit(code1, number=10000))  # First code: 0.004960464000000005
print("Second code:", timeit(code2, number=10000))  # Second code: 0.004208936000000003
print("Third code:", timeit(code3, number=10000)) # Third code: 0.0020833069999999995
