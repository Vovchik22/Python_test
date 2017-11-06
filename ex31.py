print('''
\t\tYou enter a dark room with two dootrs\n
\t\t\t\tDo you trough door:\n
\t\t\t\t#1 or #2
'''
)

door  = input("> ")

if door == "1":
    print("Theres a giant bear here eating a cheese cake")
    print("What do yo do?\n")
    print("1. Take the cake")
    print("2. Scream at the bear\n")

    bear = input(">> ")

    if bear == "1":
        print("the bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well doing {bear} is probably better ")
        print("Bears runs away")

elif door == "2":
    print ("You stare into the endless abyss. Choose number.")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revovers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity =="2":
        print("Your body survives powered by a mind")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool")
        print("Good job!")

else:
    print("you stuble around and fall on a knife")
