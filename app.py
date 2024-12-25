import sys


# print(sys.argv)  # prints the list of command line arguments
# # ['/Users/muhammadibnsalyhu/Desktop/CODING/learn_python/Section-3/23-cmd-line-args/app.py']
# # the list must always have at least one element which is the name of the script

if len(sys.argv) == 1:
    print("USAGE: python app.py <password>")
else:
    password = sys.argv[1]
    print(f"Password: {password}")
    
    
