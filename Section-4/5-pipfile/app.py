

# ╰─ pipenv --venv                                                                                             ─╯
# zsh: command not found: pipenv
# FIX:
# brew install pipenv

# pipenv install
# pipenv --venv

# /Users/myusername/.local/share/virtualenvs/learn_python-vauFCfNC

# vscode settings:

#    "python.pythonPath": "/Users/myusername/.local/share/virtualenvs/learn_python-vauFCfNC/bin/python3",
#   "python.linting.enabled": true, // enable/disable linting 


# if you want pipenv to use the system python version or ignore the pipfile, you can use the --python flag to specify the python version you want to use:
# pipenv --python 3.7

# pipenv install --dev # install the development dependencies
# pipenv install --ignore-pipfile # ignore the pipfile and install the dependencies from the lock file
# pipenv install --deploy # install the dependencies from the lock file and raise an error if the lock file is out of date
# pipenv install --system # install the dependencies globally
# pipenv install --sequential # install the dependencies in sequential order
# pipenv install --skip-lock # install the dependencies without generating a lock file
# pipenv install --three # install the dependencies using python3
# pipenv install --two # install the dependencies using python2
# pipenv install --clear # uninstall all the dependencies
# pipenv install --verbose # show verbose output
# pipenv install --bare # install the dependencies without dev dependencies

