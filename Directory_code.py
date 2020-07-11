"""Question 1
The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py"."""

comments = "# Start of a new Python program"
with open(filename, 'w') as file:
    filesize = file.write(comments)
return (filesize)

print(create_python_script("program.py"))



"""The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms"""

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename,'w') as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))


"""4.Question 4
The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified."""

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  if not os.path.exists(filename):
    open(filename,'w')
  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  stwr=str(datetime.datetime.fromtimestamp(timestamp))
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(stwr[0:10]))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd



"""5.Question 5
The parent_directory function returns the name of the directory that's located just above the current working directory. Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function."""


import os
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  path = os.getcwd()
  relative_parent = os.path.join(path, os.pardir)

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())


