ten_things = 'Apples Oranges Crows Telephone light Sugar '

print ("Wait there are not 10 things in that list. Lets fix it")

stuff = ten_things.split()
print ('We haev split \tten_things and get a list : ',stuff)

more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn',
            'Banana', 'Girl',  'Boy']

while len(stuff) !=10:
    next_one = more_stuff.pop()
    print("adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now")

print('There we go: ', stuff)

print ("Lets do some things with stuff")

print(stuff [1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what& cool!
print('#'.join(stuff[3:5]))
