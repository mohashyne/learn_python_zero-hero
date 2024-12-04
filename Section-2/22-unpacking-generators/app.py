# unpacking operators
# unpacking list
numbers = [1, 2, 3, 4, 5]
print(numbers) # [1, 2, 3, 4, 5]
print(*numbers) # unpacking list 1 2 3 4 5
print(1, 2, 3, 4, 5) # 1 2 3 4 5 unpacking list manually 


# unpacking range
values = list(range(5))
print(values) # [0, 1, 2, 3, 4]
print(*range(5)) # 0 1 2 3 4

values_list = [*range(5), *"Hello"]
print(values_list) # range(0, 5)
print(*values_list) # 0 1 2 3 4 H e l l o




# unpacking multiple lists
first_list = [1, 2, 3]
second_list = [4, 5, 6]
multiple_values = [*first_list, *second_list]
print(multiple_values) # [1, 2, 3, 4, 5, 6]
print(*multiple_values) # 1 2 3 4 5 6


# unpacking multiple dictionaries
first_dict = {"x": 1}
second_dict = {"x": 10, "y": 2}
combined = {**first_dict, **second_dict, "z": 3}





