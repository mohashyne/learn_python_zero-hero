items = [  
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
# MAP
prices  = list(map(lambda item: item[1], items)) # <map object at 0x7f9b1c6b3d90> 
print(prices)
# COMPREHENSION
mapped_prices  = [item[1] for item in items] # [10, 9, 12]




# FILTER
filtered  = list(filter(lambda item: item[1] >= 10, items)) # <map object at 0x7f9b1c6b3d90> 
print(filtered) # [[('Product1', 10), ('Product3', 12)]
# COMPREHENSION
filtered_products  = [item for item in items if item[1] >= 10] # [('Product1', 10), ('Product3', 12)]
print(filtered_products) # [('Product1', 10), ('Product3', 12)]

