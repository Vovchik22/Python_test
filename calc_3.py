def welcome ():
    print ('''
    welcome to the calculator
    ''')
welcome()

def calculate ():
    operation = input('''
+ for adding
- for substraction
* for multiply
/ for division

    ''')

    number_1 = int(input('please enter the first number: '))
    number_2 = int(input('please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('you have not type a valid operator, please run a programm again')

    again()

def again():
        calc_again = input('''
        Do you want to calculate again?
        Type Y or N
        ''')

        if calc_again.upper()== 'Y':
            calculate()

        elif calc_again.upper() == 'N':
            print('see you later')
        else:
            again()

calculate()
