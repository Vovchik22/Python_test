ten_things  = "Apples Oranges Crows Telephone Light Sugar"

print ("There are not 10 things in that list. Lets fix it")

stuff = ten_things.split(' ')
more_stuff = ['day', 'night', 'song', 'frisbee',
             'corn', 'banana', 'girl', 'boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ",  next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")

print(" there we go: ", stuff)

print("Lets do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
