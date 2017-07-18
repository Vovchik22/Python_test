'''
def multiply(*args):
    z = 1
    for num in args:
        z*=num
    print (z)

multiply (4, 5)
multiply (10, 9)
multiply (4, 5)
multiply (0, 1)
multiply (1, 2, 2, 3, 5)


def print_kwargs(**kwargs):
        print(kwargs)

print_kwargs(kwargs_1='Shark',kwargs_2=4.5,kwargs_3=True)
'''
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))

'''
print_values(
            name_0 = "alex",
            name_1 = "Grey",
            name_2 = "Happer",
            name_3 = "Remy",
            name_4 = "Val"
        )
'''

'''
def some_args(arg_1, arg_2, arg_3):
    print('arg_1: ', arg_1)
    print('arg_2: ', arg_2)
    print('arg_3: ', arg_3)

args = ('Sammy', 'Cassy', 'Alex')
some_args(*args)
'''

def some_args(arg_1, arg_2, arg_3):
    print('arg_1: ', arg_1)
    print('arg_2: ', arg_2)
    print('arg_3: ', arg_3)
my_list = [2, 3]
some_args(1, *my_list)
