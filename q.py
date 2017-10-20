from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copy from {from_file} to {to_file}")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the outputfile exist? {exists(to_file)}")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
print(len(to_file))
print(len(from_file))
