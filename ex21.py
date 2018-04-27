def add (a, b):
    print(f"Add {a} + {b}")
    return a + b

def sub (a, b):
    print(f"sub {a} - {b}")
    return a - b

def mult (a, b):
    print(f"mult {a} * {b}")
    return a * b

def div (a, b):
    print(f"Add {a} / {b}")
    return a / b

print('Lets do some math')

age = add(30,40)
height = sub(180,50)
weight = mult(30,20)
iq = div(200,100)

print(f"age: {age}, height: {height}, weight: {weight}, iq: {iq}")

print("Here ia a puzzle")

what = (add(age, sub(height, mult(weight, div(iq, age )))))

print("what: ",what)
