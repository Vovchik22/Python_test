things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)

print(sum([i for i in range (1,1000) if (i % 3 == 0 or i % 5 == 0) ]))


stuff = {'name': 'Valdimir', 'surname': 'Naydonov', 'age': 32, 'height ':  6 * 12 + 2 }
print (stuff)

print('age:', stuff['age'])

stuff['city']  = 'Kiev'

print('city:', stuff['city'])
