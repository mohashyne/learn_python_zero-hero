list1 = [10, 20, 30]
list2 = [40, 50, 60]
list3 = ["yellow", "crimson", "blue"]

paired_list = list(zip(list1, list2))
print(paired_list) # <zip object at 0x7f9b1c6b3d90>
print(paired_list) # [(10, 40), (20, 50), (30, 60)]


# or
paired_add_list = zip("abc", list1, list3, ["new", "used", "new"])
print(list(paired_add_list)) # [('a', 10, 'yellow', 'new'), ('b', 20, 'crimson', 'used'), ('c', 30, 'blue', 'new')]


p1, p2, p3, p4 = ("abcd"), [10, 15, 20, 25], ["t-shirt", "shoe", "shorts", "socks"], ["red", "yellow", "blue", "crimson"]

products  = list(zip(p1, p2, p3, p4))
print(products)