'''
class NegValException(Exception):
    pass

    try:
        val = int(input("pos number:  "))
        if val < 0:
            raise NegValException('Neg val: ' + str(val))
        print(val + 10)
    except NegValException as e:
        print(e)
'''
'''
with open ('test.txt', 'r')
    for line in f:
        print(line)
'''
