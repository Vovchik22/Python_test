# create a mapping of atste to abbrevation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# craete a basic set of states and some cities in them

cities = {
    'CA': 'San Fransisco'
    'MI': 'Detroit'
    'FL': 'Jacksonville'
}

# add some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some states
print('----' * 10)
print('NY state has: ', cities['NY'])
print('OR state has: ', cities['OR'])

#print some states
print('----' * 10)
print('Michigan abbreveation is: ', states['Michigan'])
print('Florida abbreveation is: ', states['Florida'])
