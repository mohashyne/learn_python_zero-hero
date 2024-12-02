def increment(number, by):
    return number + by
    

print(increment(2, 3))



# Example of a tuple
my_tuple = (1, 2, 3, "Python", 4.5)
print(my_tuple[0])  # 1

empty_tuple = ()  # Empty tuple
single_element_tuple = (5,)  # Tuple with one element (note the trailing comma)
mixed_tuple = (1, "Hello", 3.14)

# Tuple unpacking
my_tuple = (1, 2, 3)
a, b, c = my_tuple  # Unpack the tuple into variables
print(a, b, c)  # Output: 1 2 3




def multiply(num: int, by: int  = 1) -> tuple:
    return (num, num * by) # 5


print(multiply(2))  # (2, 6) if we don't pass the second argument the value of by will be set to 1 by  default