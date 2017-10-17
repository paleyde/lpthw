from sys import argv

script, input_file = argv

def print_all(y):
 print y.read()

def rewind(y):
 y.seek(0)


def print_only_a_line(line_count, y):
 print line_count, y.readline()

current_file = open(input_file)

print "First print the whole file:\n"

print_all(current_file)

print "Now rewind or kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_only_a_line(current_line, current_file)

current_line = current_line + 1
print_only_a_line(current_line, current_file)

current_line = current_line + 1
print_only_a_line(current_line, current_file)
