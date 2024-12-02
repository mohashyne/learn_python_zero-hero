letters = ["a", "b", "c"]

first, second, last = ["a", "b", "c"]

print(second) # b
print(first)  #  a
print(last)  # c

print(first, second, last) # a b c


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first_num, *middle_num, last_num = numbers

print(first_num, last_num)
print(middle_num)



range_numbers = list(range(20))
first_range, second_range, *other_range = range_numbers

print(first_range)
print(second_range)
print(other_range)