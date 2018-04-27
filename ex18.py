def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} and arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f'arg1: {arg1} and arg2 {arg2}')

def print_one(arg1):
    print(f"Just one arg: {arg1}")

def no_args():
    print("No args")

print_two("222", "222")
print_two_again("Pervyi", "Vtoroy")
print_one("Tolko_odin")
no_args()
