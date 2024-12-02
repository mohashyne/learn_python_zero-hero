numbers = [1, 1, 2, 3, 4, 4, 5, 4, 7, 9, 9]
unique_numbers = set(numbers)
print(unique_numbers) # {1, 2, 3, 4, 5, 7, 9}
print(type(unique_numbers)) # <class 'set'>
print (len(unique_numbers)) # 7

#  we can use curly braces to create a set
new_numbers = {1, 2, 3, 4, 5, 6, 7, 9, 8, 9, 7, 7}
new_numbers.add(8)
print(new_numbers) # {1, 2, 3, 4, 5, 6, 7, 8}
print (len(new_numbers)) # 8



# Example 2
nums = [1, 1, 2, 3, 4]
first = set(nums)
second = {1, 5}

# this will return a new set of all the items that are either in first set and second (union)
print(first | second) # {1, 2, 3, 4, 5} 

# similarities
print(first & second) # {1}

# difference ( this first sset has this additional numbers that we don't have in the second)
print(first - second) #{2, 3, 4}

# symetric difference (items in the first and second, but not both)
print(first ^ second) # {2, 3, 4, 5}

# UNLIKE list , SETS are unordered so you can't get index values like: first[0] NOT IN SEQUENCE, except

if 1 in first:
    print("Yes")



# to itterate we need to convert to list
print(list(first)[3])
    

