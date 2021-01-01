# This is an "import" that adds functions to Python
# The fuctions constitute a "module" of codes.
# Modules can also be called "libraries".
# "argv" is the #arguement variable" that holds
# variables that you send in (or pass) to Python.
from sys import argv
#This line "unpacks" argv into four variables from left to right.
script, filename = argv
# when txt is printed the file will be opened.
txt = open(filename)
# prints statement: Here's your file along with the filename; and content of file.
print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
