# for loop
# while loop


for x in "Python":
    print(x)


alphabets = ["a", "b", "c", "d"]
for a in alphabets:
    print(a)  # a b c d


for n in range(5):
    print(n) # 0 1 2 3 4


for num in range(2, 5):
    print(num) # 2 3 4

# RANGE
print(type(range(5))) #  range(0, 5)  range dose not return a list
# Range takes  a very small amount of memory, because they create new numbers from the range  unlike list
# LIST
print([1, 2, 3, 4, 5]) #  [1, 2, 3,  4, 5]



for even in range(0, 10, 2):
    print(even) # 2 4 6 8


# num = [1, 2, 3, 4, 5]
# for i in num:
#     if i % 2 == 0: print(f"{i}Even Number")
# else:
#     print(f"{i} is Odd Number")
