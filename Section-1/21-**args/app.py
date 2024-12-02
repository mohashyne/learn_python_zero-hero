def save_user(**user):
    print(user["name"])# prints the keyword arguments as a dictionary
    
save_user(id=1, name="Kristine", age=12, role="admin") # {'name': 'Kristine', 'age': 12, 'role': 'admin'} 