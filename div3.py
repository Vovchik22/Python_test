'''
try:
    import chardet
except ImportError:
    chardet = None
    '''
'''
try:
    from xml import etree
except ImportError:
    import xml.etree.ElementTree as etree
    '''
'''
if __name__ == '__main__':
    print(approximate_size(1000000000000, False))
    print(approximate_size(1000000000000))
'''
'''
def is_it_true(anything):
    if anything:
        print('yes it is true')
    else:
        print('no it is not true')
'''
'''
a  = int(input("number: ""))
if a < 0 :
    print("Neg")
elif a == 0:
    print("Zero")
else:
    print("Pos")
'''
'''
print ("Start")
try:
    val = int(input("input number: "))
    tmp = 10/val
    print(tmp)
except ValueError as ve:
    print("ValueError {0}".format(ve))
except ZeroDivisionError as zde:
    print("ZeroDivisionError {0}".format(zde))
except Exception as ex:
    print("Error {0}".format(ex))
print("Stop")
'''
try:
    f = open("tmp.txt", "r")
    for line in f:
        print(line)
    f.close()
except Exception as e:
    print(e)
else:
    print("file was readed")     
