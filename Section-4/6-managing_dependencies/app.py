# managing dependencies

# pipenv graph # show the dependency graph
# pylint==3.3.3
# ├── astroid 
# │   └── typing_extensions 
# ├── dill 
# ├── isort 
# ├── mccabe 
# ├── platformdirs 
# ├── tomli 
# ├── tomlkit 
# └── typing_extensions 
# requests==2.32.3
# ├── certifi 
# ├── charset-normalizer 
# ├── idna 
# └── urllib3

# pipenv check # check for security vulnerabilities 
# pipenv update --outdated # update the outdated dependencies

# if it show you the latest version of the package, but fails to update, that means it is not compatible with the other packages in the lock file. i.e 2.9.x compared to 2.8.0

# but if the one on your pipfile is 2.x, and the latest is 2.30.x, it will update to the latest version

# pipenv update requests # update a specific package