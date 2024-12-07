
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)   # Age cannot be 0 or less.
    
    
# The raise statement is used to raise an exception.    
# but you are not advised to raise exceptions this way, in your code.
# You should raise exceptions only when you have to.
# there are better ways to handle errors in your code.
# you should use exceptions to handle exceptional cases.
# you should use exceptions to handle unexpected cases.
# you should use exceptions to handle errors that you cannot recover from.
# you should use exceptions to handle errors that you cannot handle.
# you should use exceptions to handle errors that you cannot ignore.
# you should use exceptions to handle errors that you cannot suppress.
# you should use exceptions to handle errors that you cannot silence.
# you should use exceptions to handle errors that you cannot mask.     