fruits = ['apples', 'oranges', 'apricots', 'pears', ]
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']
the_count = [1, 2, 3, 4, 5]

for number in the_count:
    print (f'This is count for {number}')

for fruit in fruits:
    print (f"A fruit type is {fruit}")

for i in change:
    print(f'I got {i}')

elements = list()

for i in range(0,101,50):
    print (f"addding {i} to the new list")
    elements.append(i)
    print (f"{i}")
    print(elements)
