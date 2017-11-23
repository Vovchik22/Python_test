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
    'CA': 'San Fransisco',
    'MI': 'Detroit',
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
print('-' * 10)
print('Michigan abbreveation is: ', states['Michigan'])
print('Florida abbreveation is: ', states['Florida'])

# do it using the state then cities dcit
print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} is abbreviation {abbrev}')

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'{abbrev} has the city {city}')

#now do both and at the ame time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f'{state} state is abbreviation {abbrev}')
    print(f'and has city {cities[abbrev]}')

print('-' * 10)
#safely get a abbreviation by state that might not be there

state = states.get('Texas')

if not state:
    print('Sorry, no Texas')
# get a city with default vakue
    city = cities.get ('TX ', 'Does Not Exist')
    print(f'the city for the state "TX" is: {city}')
