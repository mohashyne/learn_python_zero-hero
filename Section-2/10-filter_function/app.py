items = [  
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

filtered  = list(filter(lambda item: item[1] >= 10, items)) # <map object at 0x7f9b1c6b3d90> 
print(filtered) # [[('Product1', 10), ('Product3', 12)]
