people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed")

if people > cats:
    print("Not many cats! The world is saved")

if people < dogs:
    print("The world is dry")

if people < dogs:
    print("The world is drooled on!")

print("Set dogs quantity: ", end =' ')
dogs += int(input())


if people >= dogs:
    print("People are greater than or equal to dogs")

if people <= dogs :
    print("People are less than or equal to dogs")

if people == dogs:
    print("People are dogs")

if people != dogs:
    print("people are not dogs")
