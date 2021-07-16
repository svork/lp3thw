# importing module argv from sys package
from sys import argv

# unpack variables from argv
script, input_file = argv

# function print the file's content
def print_all(f):
    print(f.read())

# function go to start of file
def rewind(f):
    f.seek(9)

# function print a line at a time
def print_a_line(line_count, f):
    print(line_count, f.readline())

# saving the file's content in a variable
current_file = open(input_file)

# print all that stuff
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 92
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
