# Tuple

# what is tuple, how to create a tuple and difference between tuple and list
# tuple is a collection of ordered and immutable elements
# tuple is a data structure that is similar to a list
# tuple is a sequence of elements that is enclosed in parentheses

# create a tuple
tuple = (10, 20, 30)
tuple = 10, 20, 30
tuple = ()
tuple = (10,)
tuple = 10,
tuple = tuple((10, 20, 30))
tuple = tuple([10, 20, 30])

concat_tuple = (10, 20, 30) + (40, 50, 60)
print(concat_tuple) # (10, 20, 30, 40, 50, 60) 

duplicate_tuple = (10, 20, 30) * 3  
print(duplicate_tuple) # (10, 20, 30, 10, 20, 30, 10, 20, 30)   

# access elements in a tuple
tuple = (10, 20, 30)
print(tuple[0]) # 10
print(tuple[1]) # 20
print(tuple[2]) # 30
print(tuple[-1]) # 30   

# tuple slicing
tuple = (10, 20, 30, 40, 50)    
print(tuple[0:3]) # (10, 20, 30)
print(tuple[1:4]) # (20, 30, 40)
print(tuple[2:5]) # (30, 40, 50)

# tuple methods
tuple = (10, 20, 30)
print(len(tuple)) # 3
print(tuple.count(10)) # 1
print(tuple.index(20)) # 1
print(tuple.index(30)) # 2
print(tuple.index(40)) # ValueError: 40 is not in list


# tuple unpacking
tuple = (10, 20, 30)    
a, b, c = tuple
print(a) # 10   
print(b) # 20

# where do we use tuple in real life applications
# tuple is used to store a collection of elements that should not be changed
# tuple is used to store a collection of elements that should not be modified
# tuple is used to store a collection of elements that should not be updated
# tuple is used to store a collection of elements that should not be deleted
# tuple is used to store a collection of elements that should not be added
# tuple is used to store a collection of elements that should not be sorted
# tuple is used to store a collection of elements that should not be reversed
# tuple is used to store a collection of elements that should not be filtered
# tuple is used to store a collection of elements that should not be mapped
# tuple is used to store a collection of elements that should not be reduced
# tuple is used to store a collection of elements that should not be searched