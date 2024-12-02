# and
# or
# not

name = " Muhammad"

if not name.strip():
    print("Name is empty")
else:
    print(f"{name.title()}'s Name is available")

age = 25
# if age >= 18 and age  < 65:
#     print("Eligible")
#

# REFACTOR
if 18 <= age < 65:
    print("Eligible")

# In Python, you can chain comparisons
# like this.The condition
#
# 18 <= age < 65 is the same as:
#
#     if (18 <= age) and (age < 65):


