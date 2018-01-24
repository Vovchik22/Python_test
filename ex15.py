
# take a variable from sys, must type filename.txt
from sys import argv
# start script and choose filename
script, filename = argv
# open choosed .txt
txt = open(filename)

print(f"here`s your file: {filename}")
print(txt.read())


# should type a filename .txt again
print("type the file again:")
file_again = input("> ")

txt.again = open(file_again)
# open a .txt file again
print(txt_again.read())
