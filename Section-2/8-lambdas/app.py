# lambda functions

# lambda functions are small anonymous functions
# they can have any number of arguments, but can only have one expression
# syntax: lambda arguments : expression
# lambda functions can be used wherever function objects are required
# they are syntactically restricted to a single expression
# semantically, they are just syntactic sugar for a normal function definition
# like a nested function definition, but with a different syntax
# lambda functions are often used as arguments to higher-order functions
# like map, filter, and reduce

# lambda functions are used to create small, one-time, anonymous function objects in Python
# they are useful for writing short, throw-away functions   


# example of a lambda function  
# lambda arguments : expression
# this lambda function takes one argument x and returns x + 10
# the lambda function is assigned to the variable f
f = lambda x : x + 10
print(f(5)) # 15

sum = lambda x, y : x + y 


# INSTEAD OF  WRITING A FUNCTION LIKE THIS:
items = [  
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

def sort_item(item):
#   return item[1] # 10, 9, 12
    return item[1]

items.sort(key=sort_item) # [('Product2', 9), ('Product1', 10), ('Product3', 12)]
print(items)   


# YOU CAN WRITE A LAMBDA FUNCTION LIKE THIS:
items_two = [  
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items_two.sort(key=lambda item: item[1]) # [('Product2', 9), ('Product1', 10), ('Product3', 12)]
print("This is sorting  using lambdas:",items_two)