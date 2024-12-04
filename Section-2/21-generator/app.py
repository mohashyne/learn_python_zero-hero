from sys import getsizeof as size

# Generator function
# what is generator function and why is it recommended when using large data sets, rather than list comprehension

# generator function is a function that returns an iterator object, which can be used to iterate over elements of a sequence one at a time.
# generator function uses yield keyword instead of return keyword to return the value.
# generator function does not store the entire sequence in memory, but generates the value on the fly.
# generator function is recommended when working with large data sets, because it is memory efficient.


values = [x * 2 for x in range(1000000)]
print("Size of list comprehension:", size(values)) # 8697464 bytes

values = (x * 2 for x in range(1000000))
print(values) # <generator object <genexpr> at 0x7f9c8d9e5e40>
print("Size of generator function:", size(values)) # 128 bytes


# because generator function does not store the entire sequence in memory, you will not be able to access the elements by index.
# you can only iterate over the elements using a for loop or next() function. so if you use the len function, you will get an error.