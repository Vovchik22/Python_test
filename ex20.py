from sys import argv
script, input_file = argv  # pre-start recognise script and file

def print_all(f):   # read recognised file
    print( f.read())

def rewind (f): # define position in file in BYTES
    f.seek(0)

def print_a_line(line_count, f):   # define variable number of a line and a second argument defines a line (first as a default)
    print (line_count, f.readline())

current_file = open(input_file) # with this variable we open current file which recognised at pre-start script

print("Lets print a whole file: \n")

print_all(current_file) # function opened file and read it

print("Now lets rewind")

rewind(current_file)   # fuction recognised position

print("lets print three lines")

current_line = 1  # variable set number 1
print_a_line(current_line, current_file) # function for each further line we add line in opened file

current_line = current_line + 1 # add a number to a line
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_file.close() # close current file after all proceduders
