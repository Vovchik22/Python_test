from sys import exit

def gold_room ():
    print ('This a room is full of gold. How much do you take?')

    choice  = input('\t\t>>>  ')
    if '0' or '1' in choice:
        how_much  = int(choice)
    else:
        dead("Man, learn to type a numbers")

    if how_much in range (1,50):
        print('You are not too greedy')
        exit(0)
    else:
        dead('You are greedy')

def bear_room ():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    while  True:
        choice = input("\t\t>>>   ")

        if choice == 'take money':
            dead('the bear slap your face')
        elif choice == 'taunt bear' and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == 'taunt bear' and bear_moved:
            dead ('The bear gets piised off and chews your leg')
        elif choice == 'open door' and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means")
            exit()

def chtulhu_room():
        print("Here you see the great evil Cthulhu.")
        print("He, it, whatever stares at you and you go insane")
        print("Do you flee for your life or eat your head?")

        choice = input ("\t\t>>>")

        if "flee" in choice:
            start()
        elif "head" in choice:
            dead('Well you are dead')
        else:
            chtulhu_room()

def dead (why):
    print (why, 'good job')
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input('\t\t>>>  ')

    if choice == 'left':
        bear_room()
    elif choice == 'right':
        chtulhu_room()
    else:
        dead('You are stumble around')

start()
