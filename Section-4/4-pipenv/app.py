"""
This module demonstrates an example function that prints a message.
"""
import requests

response = requests.get('https://api.github.com')
print(response)

# pipenv is equivalent to npm in node.js  or yarn in node.js or bundler in ruby
# pipenv is a dependency manager for python projects

# to install pipenv run the following command
# pip3 install pipenv
# pipenv --help



# to install a package in the virtual environment run the following command
# pipenv install requests==2.30.0

# pipenv install requests~=2.30.0  will create a Pipfile.lock file which will lock the version of the package to 2.30.x
#  to access the virtual environment and the path run the following command
# pipenv shell will activate the virtual environment
# pipenv --venv will print the path to the virtual environment directory


# but remember we installed pipenv in the global environment so we can use it to install packages globally
#  idea
