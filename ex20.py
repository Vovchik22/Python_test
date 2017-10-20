from sys import argv # impport from sys module arguements
script, input_file = argv  # define script and imported file

def print_all (f):   # define function with arg f  than execute function and read file
    print(f.read())  # read file

def rewind(f):   # define function that we can see what in the opened file
    f.seek(0)    #

def print_a_line(line_count, f):  # function with args, can
    print(line_count, f.readline()) # exccute line count from function print_a_line, show line

current_file = open(input_file)

print("lets print the hole file: \n")

print_all(current_file)


print("now lets rewind, kind of like a tape")

rewind(current_file)

print("lets print three lines")

current_line = 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

'''
# Open a file
fo = open("foo.txt", "r+")
print ("Name of the file: ", fo.name)

line = fo.readlines()
print ("Read Line: %s" % (line))

# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print ("Read Line: %s" % (line))

# Close opened file
'''
