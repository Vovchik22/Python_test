print("""
hello!!!
please choose what you want to do
1 - choice is for playing piano\n
2 - choice is for playing guitar\n
3 - choice is for playing VR game\n
""")

choice = input(">>>   ")


if choice == "1":
     print("You playing piano")
elif choice == "2":
    print("You playing guitar")
elif choice == "3":
    print("You playing VR game")
else:
    print("Just choose from 1 to 3")


print(""""
Depends of previous choice.
Choose playing melody
\t\t1 - for melody  on piano
\t\t2 - for melody  on guitar
\t\t3 - noting
""")

melody = input(">>>  ")

piano = "1"
guitar = "2"

if melody == piano:
    print("You are playing guitar piano")
elif melody == guitar:
    print("you playing guitar")
else:
    print("You are playing VR Game")
