# define all numbers that could be divisible

def div (number):
    for i in range(2, number):
        if number % i != 0:
            return False
    return True

number  = int(input('Enter looking number:   '))
while True:
    if div (number):
        break
    number += number

print(number)
