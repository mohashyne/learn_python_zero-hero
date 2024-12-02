# args

def multiply(*list):
   total = 1
   for num in list:
      total *= num 
   return total



print(multiply(2, 3, 5, 7)) # 210

