
x = "there are %d types of people" % 10
binary = 'binary'
do_not = 'dont'
y = "those who know %s and those who %s" % (binary, do_not)

print (x)
print (y)

print ("i said %r." % (x))
print ("i said also: '%s'" % (y))

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print (joke_evaluation % hilarious)

w = "this is the lefy side of ...."
e = "a string with a right side."

print (w + e)
