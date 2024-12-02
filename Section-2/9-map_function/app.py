items = [  
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


# price = []
# for item in items:
#     price.append(item[1])   
    
# print(price) # [10, 9, 12]  

# map() function
# map() function is a built-in function that applies a given function to all items of an iterable and returns an iterator
# syntax: map(function, iterable)
# map() function can be applied to more than one iterable

prices  = map(lambda item: item[1], items) # <map object at 0x7f9b1c6b3d90> 
for item in prices:
    print(item) # 10, 9, 12
print(prices) # <map object at 0x7f9b1c6b3d90> 

# sine this is an iterator, we can convert it to a list
print(list(prices)) # [10, 9, 12]



# or  prices  = list(map(lambda item: item[1], items)) # [10, 9, 12]

 