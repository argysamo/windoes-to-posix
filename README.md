# Description
This projects is intended to be executed on a Windows platform.
It transforms a windows path to posix and vice versa.  
It reads the clipboard and in case it finds a path it transforms it and replaces the clipboard. 

# How to run
As mentioned above this tool is only intended for `Windows`. 
In order to make the tool available on your system you need to perform the followings:
- Clone the project and visit the directory
- Create a python venv: `python3 -m venv venv`
- Activate the venv: `venv/Scripts/activate.bat`
- Install all dependencies: `pip install -r requirements.txt`
- Create the .exe of the tool: `pyinstaller main.py`
- Navigate to the freshly created `dist` directory and create a shortcut of the `main.exe`

Running the `main.exe` will update your clipboard when a path is found. 