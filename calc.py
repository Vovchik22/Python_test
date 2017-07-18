def welcome():
 print ('''
welcome to calculator
''')
welcome()

#define our function
def calculate ():
   operation = input('''
please type in the math operation you would you like to complete
+ for additing
- for substraction
* for multiplication
/ for division
''')


   number_1  = int(input('enter your first number: '))
   number_2  = int(input('enter your second number: '))


#addition
    if operation == '+':
       print ('{} + {} = '.format(number_1, number_2))
       print (number_1 + number_2)

#substraction
    elif operation == '-':
       print('{} - {} = '.format(number_1, number_2))
       print(number_1 - number_2)

#multiplication
elif operation == '*':
    print ('{} * {} = '.format(number_1, number_2))
    print (number_1 * number_2)

#division
elif operation == '/':
    print ('{} / {} = '.format(number_1, number_2))
    print (number_1 / number_2)

else:
    print ("you have not type a valid operator, please run program again.")

    # call calculate outside  the function
    calculate ()

    #define again () function to ask users if they want to use the calculator again
def again():
        # take input from users
        calc_again = input ('''
        Do you want to calculate again ?
        PLease type Y for Yes or N for No
        ''')
 # Accept "y" or Y by adding str.upper ()

        # if user type Y, run the calculate () function
if calc_again.upper () == 'Y':
    calculate()

        # If user type N, say goodbue to user and end the program
elif calc_again.upper() == 'N':
    print ("see you later")

# if user types another key, run the function again
else:
    again()

# Call calculate () outside of the function
calculate ()
