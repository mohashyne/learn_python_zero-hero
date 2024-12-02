# queues

from collections import deque
queue = deque([]) # create an empty queue
queue.append(1) # add 1 to the queue
queue.append(2) # add 2 to the queue
queue.append(3) # add 3 to the queue
print(queue) # deque([1, 2, 3])
print(queue.popleft()) # 1
print(queue) # deque([2, 3])    
print(queue[0]) # 2   # first element in the queue  
if 2 in queue:
    print("2 is in the queue") # 2 is in the queue
    
    # OR
    
    
print("People are in the queue: ", bool(queue)) # True   # check if the queue is empty 


print("People are in the queue" if queue[1] else "This Person has left the queue")
  

# imagine a queue of people waiting to buy tickets
# to buy a ticket, you have to wait in line
# FIFO - First In First Out
# when the ticket seller is ready, they sell a ticket to the first person in line
# and the first person leaves the line
# when a new person arrives, they join the back of the line
# this is an example of a FIFO data structure
# in python, we can use a deque to implement a queue
# we can use the append method to add an element to the queue
# we can use the popleft method to remove the first element from the queue
# we can use the index 0 to access the first element from the queue
# we can use the len function to get the number of elements in the queue
# we can use the in operator to check if an element is in the queue
# we can use the remove method to remove an element from the queue
# we can use the clear method to remove all elements from the queue
# we can use the copy method to return a copy of the queue
# we can use the count method to count the number of occurrences of an element in the queue
