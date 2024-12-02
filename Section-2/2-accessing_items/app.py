letters = ["a", "b", "c", "d"]

print(letters[0]) # a
print(letters[0:3]) # ['a', 'b', 'c']
print(letters[2:3]) # ['c']
print(letters[-1]) # d

letters[2] = "g"

print(letters) # ['a', 'b', 'g', 'd']

for letter in letters:
    print(list(letter.upper()))
    
 
lett =  "hello word"    
def sum(inputs):
    total = 0
    length = len.inputs
    print(length)
    if length < 5:
        total += len
    return total    
            
            
print(sum(lett))           