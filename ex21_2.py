# formula (100 + 50/50 - 1000) / 125

def add (a,b):
    print(f"{a} + {b}")
    return  a + b

def sub(a, b):
    print(f"{a} - {b}")
    return a - b

def mult (a, b):
    print(f"{a} * {b}")
    return a * b

def div (a, b):
    print(f"{a} / {b}")
    return a / b

first = div(50,50)
second  = add(100, first)
third = sub(second, 1000)
last = div(third, 125)

if __name__ == "__main__":

    var1 = int(input("var1: "))
    var2 = int(input("var2: "))
    var3 = int(input("var3: "))
    var4 = int(input("var4: "))
    var5 = int(input("var5: "))
'''
    print("""choose operator:
            * - mult
            + - Add
            / div
            - sub
            """)
    operator = input()

if operator == '*':
    print(mult(var1,var2))
elif operator == '+':
    print(add(var1,var2))
elif operator == '/':
    print(div(var1,var2))
elif operator == '-':
    print(sub(var1,var2))
else:
    pass
'''
formula  = (div(sub(add(div(var1,var2), var3),var4),var5))
print(formula)
