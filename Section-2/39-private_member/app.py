class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(),  0) + 1

    def __getitem__(self, key):
        return self.__tags.get(key.lower(), 0)    

    def __setitem__(self, key, value):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)

    def __delitem__(self, key):
        del self.__tags[key.lower()]      
   





cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
# print(cloud.tags) # {'python': 3}
print(cloud.__tags) # 'TagCloud' object has no attribute '__tags', this is because __tags is a private member
print(cloud.__tags["PYTHON"]) # this is a key error because the key is not in the dictionary, 
# and the coverting the key to lowercase will not work

# technically, you can still access the private member by using the following syntax, it is just that they will 
# be deficult to access
print(cloud.__dict__) # {'_TagCloud__tags': {'python': 3}}
# print(cloud._TagCloud__tags) # {'python': 3}
len(cloud) # 1

cloud.add("java")
cloud.add("Java")
cloud.add("Javascript")
len(cloud) # 3

print(cloud.__tags)
