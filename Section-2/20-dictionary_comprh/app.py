values = []
for x in range(5):
    values.append(x * 2)
    

print(values)    


# dictionary comprehesion
com_values = {x: x * 3 for x in range(7)}
print(com_values)


# testing
second_values = []
{second_values.append({num: num * 3}) for num in range(5)}
print(second_values)
                 


