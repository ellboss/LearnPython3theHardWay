from sys import argv
# This is an "import" that adds functions to Python
# The fuctions constitute a "module" of codes.
# Modules can also be called "libraries".
# "argv" is the #arguement variable" that holds
# variables that you send in (or pass) to Python.
script, first, second, third = argv
#This line "unpacks" argv into four variables from left to right.

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# When you run this script, type the information for
# the variable on the same line as "python ex13.py"
