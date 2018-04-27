# create a mapping of state to abbreviation
states  = {
'Oregon': 'OR',
'Florida': 'FL',
'New York': 'NY',
'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
'CA':'San Fransisco',
'MI': 'Detroit',
'FL': "Jacksonvile"
}

# add some more sities

cities['OR'] = 'Portland'
cities['NY'] = 'New York'

# print out some cities
print('-' * 10)
print('NY state has: ', cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print('Michigan abbreviation is: ', states['Michigan'])
print('Florida abbreviation is: ', states['Florida'])

# print every state abbreviation

for state, abbrev in list(states.items()):
    l = list(states.items())
    print(l)
    print(state, abbrev)
    print(f"{state} is abrreviation {abbrev}")

# print every city in state
print ('-' * 10)
for abbrev, city in list(cities.items()):
    l = list(cities.items())
    print(l)
    print(f'{abbrev} has the city {city}')

# now do both at the same time

print('-' * 10)
for state, abbrev in list(states.items()):
    print (f'{state} state is abbreviated {abbrev}')
    print(f'and has city {cities[abbrev]}')

# safely get a abrreviation be state that might not be There
state = states.get('Texas')
if not state:
    print("Sorry, no Texas")

# get a city with a degfault value

city = cities.get('TX', 'Does not exist')
print(f'The city for the "TX" is : {city}')
