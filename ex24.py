print ('Lets practice everything')
print('You\'d need to knov \' about escapes with \\ that do:' )

poem = ("""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needds of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere is none
""")

print ("-----------------------")
print(poem)
five  = 10 - 2 + 3 - 6
print(f"This should be five {five}")

def secret_formula (started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("with a starting point of : {}".format(start_point))

print(f'we have {beans} beans, {jars} jars, {crates} crates')

start_point = start_point / 10

print(" We can also do that this way:  ")

formula = secret_formula(start_point)

print("We have {} beans, {} jars, {} crates".format(*formula))
