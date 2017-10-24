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
