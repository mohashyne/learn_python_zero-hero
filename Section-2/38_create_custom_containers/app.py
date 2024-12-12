# for example we want to get the number of tags in an article
# we can create a custom container to do this task

class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(),  0) + 1

    def __getitem__(self, key):
        return self.tags.get(key.lower(), 0)    

    def __setitem__(self, key, value):
        self.tags[key.lower()] = value

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)

    def __delitem__(self, key):
        del self.tags[key.lower()]      
   





cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags) # {'python': 3}
len(cloud) # 1

cloud.add("java")
cloud.add("Java")
cloud.add("Javascript")
len(cloud) # 3

print(cloud.tags) # {'python': 3, 'java': 2, 'javascript': 1}


#  to set number of a tag item like this:
# cloud.tags["python"] = 10 , we can create a custom container to do this task
cloud["python"] = 10

print(cloud.tags) # {'python': 10, 'java': 2, 'javascript': 1}

for key in cloud.tags:
    if cloud.tags[key] > 2:
        print(f"This tag is greater than 2: {key}: {cloud.tags[key]}")
