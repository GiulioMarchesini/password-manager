# Password Generator
This is a simple password generator written in python.
The user inserts:
* name of the website
* username
* password (or press the button to generate a random password)

When the "Add" button is pressed, the data are saved in a file called "data.txt" in the same folder of the program.

## CREATE EXE
it's necessary to install pyinstaller if it is not already installed:
<br>
for do it, open a terminal and type: pip install pyinstaller --user
<br>
for generate exe file, open a terminal and type: pyinstaller --onefile --windowed main.py

* "--onefile" creates a single executable file (packs everything into a single exe file)
* "--windowed" hides the console

in "dist" folder will be created the executable file.