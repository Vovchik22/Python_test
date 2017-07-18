from sys import argv

script, filename = argv

print(f"Were going to erase {filename}.")
print("If you dont want that, hit CTRL_C (^C).")
print("If you do want that hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Good bye!")
target.truncate()

print("Now im going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("im going to write these to the file.")

target.write (line1)
target.write("\n")
target.write (line2)
target.write("\n")
target.write (line3)
target.write("\n")

print("and finaly, we close it.")
target.close()
