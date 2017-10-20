from sys import argv
script, filename =  argv


print("operating the file....")
target = open(filename, 'w')

print ('truncating the file. Bye')
target.truncate()

print("Now, I`m going ask you foe three words")

x = '''\tThis is line 1,\n \tThis is line 2,\n \tThis is line 3\n'''

print("I`m going to write this in file")

target.write(x)

print("and finaly we close it")
target.close()
