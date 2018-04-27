from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("If you dont want that, hit CTRL-C")
print("Else, hit RETURN")

input("?  ")

print ("Opening file")

target = open(filename, 'w')


print ("truncatting the file")
target.truncate()


print ("Now I`m to ask you for the three lines")

line1 = input ("line 1:  ")
line2 = input ("line 2:  ")
line3 = input ("line 3:  ")

print("Now Im going to wtite these lines")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("Do not forget to close the file")
target.close()

print("read amendment file")

readfile = open(filename, 'r')
print(readfile.read())
