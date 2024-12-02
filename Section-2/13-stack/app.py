#  stack

# imagine a stack of plates, to remove a plate, you have to remove the top plate first
# LIFO - Last In First Out



# let use a website as an example
# when you click on a link, it takes you to a new page
# when you click on the back button, it takes you back to the previous page
# this is similar to a stack, where the last page you visited is the top of the stack
# and the first page you visited is the bottom of the stack
# when you click on the back button, it removes the top page from the stack and takes you to the previous page
# this is an example of a LIFO data structure
# in python, we can use a list to implement a stack
# we can use the append method to add an element to the stack
# we can use the pop method to remove the top element from the stack
# we can use the index -1 to access the top element from the stack

browsing_session = [] # create an empty stack
browsing_session.append(1) # add 1 to the stack
browsing_session.append(2) # add 2 to the stack
browsing_session.append(3) # add 3 to the stack
print(browsing_session) # [1, 2, 3]

last = browsing_session.pop() # remove 3 from the stack
print(last) # 3
print(browsing_session) # [1, 2]

print("top of the stack: ", browsing_session[-1]) # 2   # top of the stack
print("size of the stack: ", len(browsing_session)) # 2   # size of the stack   
print("is the stack empty: ", not bool(browsing_session)) # False   # check if the stack is empty   

    #  OR
    
if not browsing_session:
    print("disable the back button")# disable the back button if the stack is empty




# stack operations
# push - add an element to the stack
# pop - remove the top element from the stack
# peek - return the top element from the stack
# isEmpty - check if the stack is empty
# size - return the size of the stack
# clear - remove all elements from the stack
# search - search for an element in the stack
# contains - check if the stack contains an element
# copy - return a copy of the stack
# toList - return a list of the stack elements
# toArray - return an array of the stack
# toSet - return a set of the stack elements
# toQueue - return a queue of the stack elements
# toDeque - return a deque of the stack elements
# toLinkedList - return a linked list of the stack elements
# toDict - return a dictionary of the stack elements
# toTuple - return a tuple of the stack elements
# toStr - return a string of the stack elements
# toInt - return an integer of the stack elements
# toFloat - return a float of the stack elements
# toBool - return a boolean of the stack elements
# toBytes - return bytes of the stack elements
# toByteArray - return a byte array of the stack elements
# toChar - return a character of the stack elements
# toShort - return a short of the stack elements
# toLong - return a long of the stack elements
# toDouble - return a double of the stack elements
# toFloat - return a float of the stack elements
# toComplex - return a complex of the stack elements
# toHex - return a hexadecimal of the stack elements
# toOctal - return an octal of the stack elements
