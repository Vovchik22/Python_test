the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# this first kind of for-loop goes trough a list for number in the count:

for number in the_count:
    print(f"This is count {number}")

# same above

for fruit in fruits:
    print(f"a type of fruit: {fruit}")

# also we can go for mixed lists Too
# notice we have to use {} since we donts  know whats in it

for i in change:
    print(f"I got {i}")

# we can also build lists, first start an empty one
elements = []

# then use the range function to do 0 to 5 counts

for i in range (0,6):
    print(f"Adding {i} to the list")
    #append is a function thats lists understand
    elements.append(i)

# now we can print them out Too

for i in elements:
    print(f"Element was: {i}")