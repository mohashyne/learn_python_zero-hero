#  check list of pips
# pip3 list : pip3 list                                                                                                                    ─╯
# Package            Version
# ------------------ ----------
# certifi            2024.12.14
# charset-normalizer 3.4.1
# idna               3.10
# pip                24.3.1
# requests           2.30.0
# setuptools         68.2.0
# urllib3            2.3.0
# wheel              0.41.2
# with the current structure we cannot have two versions of the same package installed at the same time
# to  solve this problem we can use virtual environments

# To use different versions of the same Python package like requests for separate projects, you can use virtual environments. These create isolated Python environments where you can install specific package versions without affecting other projects or the global Python environment.

# To create a virtual environment, run the following command in the terminal:
# python3 -m venv myenv or env

# This will create a new directory called myenv in the current directory. To activate the virtual environment, run the following command:
# source myenv/bin/activate or source env/bin/activate , this will activate the virtual environment

#  on windows use the following command to activate the virtual environment
# myenv\Scripts\activate.bat or env\Scripts\activate.bat orr python -m venv env

# to deactivate the virtual environment run the following command
# deactivate

# To install packages in the virtual environment, you can use pip as usual. For example, to install the requests package in the virtual environment, run the following command:
# pip3 install requests==2.30.0

