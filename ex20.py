from sys import argv

script, input_file = argv

# prints the whole file passed
def print_all(f):
    print f.read()

# puts the offset (focus) in the initial position (because 0 is passed) of the file passed (seek)
def rewind(f):
    f.seek(0)

# prints a number of line and their equivalent line
def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 #1
print_a_line(current_line, current_file)

current_line += 1 #2
print_a_line(current_line, current_file)

current_line += 1 #3
print_a_line(current_line, current_file)