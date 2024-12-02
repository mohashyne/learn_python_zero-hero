letters = ["a", "b", "c"]


# for letter in enumerate(letters):
#     print(letter)
    
# (0, 'a')
# (1, 'b')
# (2, 'c')


# for letter in enumerate(letters):
#     print(letter[0], letter[1])
    
# 0 a
# 1 b
# 2 c    



for index, letter in enumerate(letters):
    print(index, letter)
    
# 0 a
# 1 b
# 2 c  

    
    

for index, letter in enumerate(letters):
    if letter == "c":
        print(f" index:{index} and letter:{letter} Is a cats")
    else:
        print("no cat was found in index", index)       
    