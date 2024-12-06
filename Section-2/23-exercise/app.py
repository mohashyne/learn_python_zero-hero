
from pprint import pprint

sentence = "This is a common interview question, there are multiple ways to solve this problem."
char_frequency = {}

# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1

# char_frequency_sorted = sorted(
#     char_frequency.items(),
#     key=lambda kv: kv[1],
#     reverse=True) 


# print(char_frequency_sorted[0])


sentence = "This is a common interview question, there are multiple ways to solve this problem."
char_frequency = {}

for char in sentence:
    if char != " ":  # Ignore white spaces
        if char in char_frequency: # check if the character is already in the dictionary
            char_frequency[char] += 1 # increment the count of the character if it is already present
        else:
            char_frequency[char] = 1 # add the character to the dictionary with count 1 if it is not already present

 # pprint is used to print dictionary in a better way             

# since we cannot sort dictionary, we need to convert it to list of tuples
# and then sort it
char_frequency_sorted = sorted(
    char_frequency.items(), # items() returns a list of tuples
    key=lambda kv: kv[1], # sort based on the value of the tuple (count of the character) 
    reverse=True) # sort in descending order

print(char_frequency_sorted[0]) # print the first element of the sorted list

 
 



