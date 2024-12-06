# number = [1, 2]
# print(number[3]) # This will throw an error as the index 3 is out of range

# age = int(input("Age: "))
# print(age) # This will throw an error if the input is not a number

# To solve the above issue, we can use try-except block

try:
    age = int(input("Age: "))
    print(age)
except ValueError as ex:
    print(ex)
    print(type(ex))
    print("You didn't enter a valid age.")
else:
    print("Value processed, You entered a valid age.")    
print("Execution continues") # This will be printed even if the input is not a number
# otherwise the program will stop at the print(age) line if we don't use try-except block 
