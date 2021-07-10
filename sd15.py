# import the module 'argv' from sys
from sys import argv

# get variables
script, filename = argv

# open the file, read only is the default
txt = open(filename)

# print message
print(f"Here's your file {filename}")

# print file, using the 'read' method
print(txt.read())
txt.close()
