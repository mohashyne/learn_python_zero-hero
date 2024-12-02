letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# Add items to the list
letters.append("k")
letters.append("l")

# Remove items from the list
letters.pop()       # Remove the last item
letters.pop(0)      # Remove the first item
print(letters)      # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']    

# Add items to the list
letters.insert(0, "a") # Insert at the beginning
letters.insert(3, "d") # Insert at the 4th position
print(letters)        # ['a', 'b', 'c', 'd', 'd


del letters[0] # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print(letters) # ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']


letters.remove("d") # ['b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
print(letters) # ['b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

letters.clear() # []
print(letters) # []
