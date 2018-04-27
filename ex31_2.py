print ('''
You are enter a dark room with two doors
Do you go throuth door # 1 or door # 2
''')

door  = input(' \tDoor> ')

if door == '1':
    print ('there is a bear here eating a cheese cake')
    print ('What do you do?')
    print ('1. Take  a cake')
    print ('2. Scream at the bear')

    bear = input(' \tbear > ')

    if bear == '1':
        print('the bear eats you face off. Good job')
    elif bear == '2':
        print ('The bear eats you legs')
    else:
        print (f"well, doing {bear} is probably better")
        print ("Bear runs away")
elif door == '2':
        print ('You state into the endless abyss at cthulhu retreat')
        print ('\n1. Bluberries \n2. Yellow Jacket \n3. Underastanding yelling melodies')

        insanity  = input ('> ')

        if insanity == '1' or insanity == '2':
            print ('Your body survives ')
            print ('Good Job')
        else:
            print ('The insanity rots your eyes')
else:
    print ('You are stumble around')
