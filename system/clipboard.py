import os
import time
import subprocess
from datetime import date


filename = input("Name of file: ")
optional_notes = input("Optional Notes: ")
last_copied = ""
folder = '/Users/pr-mbausr/temp/clipboard-copy/'

# Add ".md" extension if no file extension is provided
filename, extension = os.path.splitext(filename)
if not extension:
    filename += ".md"

# put the file in the notes folder
filename = folder + filename

#Main Code

subprocess.run(['pbcopy'], input=b'', encoding='utf-8') # clear clipboard

try:
    with open(filename, "a") as file:
        file.write(f'Dates: {date.today().strftime("%y-%m-%d")} \n')
        file.write(f'Notes: {optional_notes} \n\n')
    while True:
        current_copied = subprocess.check_output("pbpaste").decode().strip()
        if current_copied != last_copied:
            with open(filename, "a") as file:
                file.write(current_copied + "\n")
                last_copied = current_copied
        time.sleep(1)
except KeyboardInterrupt:
    print("Script paused or terminated.")




"""
In the case of input=b'', it is specifying an empty bytes literal as the input for the subprocess.run() command.
  This is necessary when using the subprocess.run() function with the input parameter to pass data as bytes instead of strings.

Bytes literals : represent a sequence of bytes
string literals : represent a sequence of characters


2
The os.path.splitext() function splits the path into two components: the base name and the extension. It considers the last period (".") in the path as the separator between the base name and the extension.

3. Flag variable

FLAG Variable:

first_iteration = True

try:
    while True:
        current_copied = subprocess.check_output("pbpaste").decode().strip()
        if not first_iteration and current_copied != last_copied:
            with open(filename, "a") as file:
                file.write(current_copied + "\n")
                last_copied = current_copied
        first_iteration = False
        time.sleep(1)
except KeyboardInterrupt:
    print("Script paused or terminated.")
"""
