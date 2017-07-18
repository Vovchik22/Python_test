from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}, i`m the {script} script.")
print("i`d like to ask you a few questions.")
print(f"If you like me {user_name}?")
likes = input(prompt)

print (f"where do you live {user_name}?")
lives = input(prompt)

print(f"what kind og computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me
You live in {lives}. Not sure where it is
And you have a {computer}. Nice
""")
