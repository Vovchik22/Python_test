# tell if a number is divisible by 1 to 20
def Div (number):
    for i in range (2, 21):
        if number % i != 0:
            return False
    return True


# strting number 1, check if its divisible by 1 to 20
number = 20
while True:
    if Div(number):
        break
    number +=20    # increment number

# if we found the number, stop

print(number)
