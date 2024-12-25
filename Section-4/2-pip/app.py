import requests
import json


# to install requests module
# pip3 install requests==2.30.0
# pip3 install requests==2.30.*
# pip3 install requests~=2.30.0 , this will install the latest compatible version of 2.30.x
# pip3 install requests==2.* , this will install the latest version of 2.x


# unistall requests module
# pip3 uninstall requests

# this will make a get request to google.com with a timeout of 10 seconds
response = requests.get('https://www.google.com', timeout=10)
print(response)  # this will print the response object

# this will make a get request to jsonplaceholder.typicode.com with a timeout of 10 seconds
response = requests.get(
    'https://jsonplaceholder.typicode.com/todos/1', timeout=10)
print(response)  # this will print the response object

# convert the response object to string
data_text = response.text
print(data_text)  # this will print the string

# convert the response object to a dictionary
data = response.json()
print(data)  # this will print the dictionary


