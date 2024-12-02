point = dict(x=2, y=2)

point["z"] = 10

print(point)

print(point.get("x"))


point["staff"] = ["Admin", "ict", "kano region"]

print(point.get("staff", "User Not found")) # ('Admin', 'ict', 'kano region')
print(point.get("staff2", "User Not found")) # User Not found

del point["staff"][1]

print(point) # {'y': 2, 'x': 2, 'z': 10, 'staff': ['Admin', 'kano region']}

for key in point:
    print(key, point[key])


    # OR



for key, value in point.items():
    print(key, value)    