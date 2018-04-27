from sys import argv
from os.path import exists

script, from_file, to_file  = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()
print(indata)
print(f"The input file is {len(indata)} bytes long")
print("Does the output file exist? {}".format(exists(to_file)))
print("Does the output file exist? %s" % (script))
print('For proceeding - "any key" to terminate "CTRL-C"')

input("Type>>")

out_file = open(to_file, 'w')
out_file.write(indata)

print(f'Done with {to_file}')
in_file.close()
out_file.close()

new_file = open(to_file, 'r')
new_data = new_file.read()

print(f"Checkin files  {indata==new_data}")
