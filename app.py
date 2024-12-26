import sys
import requests


# print(sys.argv)  # prints the list of command line arguments
# # ['/Users/muhammadibnsalyhu/Desktop/CODING/learn_python/Section-3/23-cmd-line-args/app.py']

response = requests.get('https://api.github.com')
print(response)
    
    
