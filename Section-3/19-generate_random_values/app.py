import random
import string


print(random.random())  # 0.20592091134259494
print(random.randint(1, 10))  # picks any number from range 1-10
print(random.choice([1, 3, 7, 2, 9]))  # picks any number from list
print(random.choices([1, 2, 3, 4, 5], k=3))  # 3 numbers randomly
# i.e let say we want to pick 4letters for our password
print(random.choices("abcdefghi", k=4))
# this  will return random 4letter list for our password ['g', 'a', 'a', 'b']

# to convert it to a string instead of a list
print("Your new Password is:", "".join(random.choices(f"{string.ascii_letters}{string.digits}{string.punctuation}", k=12)))


print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits) # 0123456789
print(string.punctuation) # !"#$%&'()*+,-./:;<=>?@
print(string.ascii_lowercase) # abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase) # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters + string.digits + string.punctuation) # all possible characters


numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)