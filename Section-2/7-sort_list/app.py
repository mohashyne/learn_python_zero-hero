numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers) # [2, 3, 6, 8, 51]

numbers.sort(reverse=True)
print(numbers) # [51, 8, 6, 3, 2]


# # sorted() function   # sorted() function is a built-in function that returns a new sorted list from the elements of any iterable.  and dose not change the original list
new_numbers = [3, 71, 22, 8, 6, 9]

sorted(new_numbers)
print(new_numbers) # [3, 6, 8, 9, 22, 71]


print(sorted(new_numbers, reverse=True))



items = [  
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]


items.sort()    # [('Product1', 10), ('Product2', 9), ('Product3', 12)]

def sort_item(item):
#   return item[1] # 10, 9, 12
    return item[1]

items.sort(key=sort_item) # [('Product2', 9), ('Product1', 10), ('Product3', 12)]

print(items)    


