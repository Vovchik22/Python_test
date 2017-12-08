
a = 0
b = 1
fibo = 0

while b <= 4000000:
    if b % 2 == 0:
        fibo += b
    a,b = b, a + b
print(fibo)
