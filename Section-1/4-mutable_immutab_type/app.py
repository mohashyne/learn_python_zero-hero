x = 1

print(id(x)) # 4419092720 ( this is the address of the memory location where it is stored and it immutable)


x = x + 1
print(id(x)) # 4419092752

# All the built-in primitive types are immutable , if you try to update any variable python interpreter will allocate a new memory for it with a new id, at  some point python garbage collector will release the first memory  and "X" will reference the new memory location.



# MUTABLE TYPE (using list)
y = [1, 2, 3, 4]
print(id(y)) # 4423232576

y.append(5)
y.pop(2)

print(y) # [1, 2, 4, 5]

print(id(y))  # 4423232576

