'''
n = 21
a = [True] * n

a[0] = a[1] = False

for k in range (2, n):
    if a[k]:
        print(k)
        for m in range (int(2*k), n, k ):
            a[m] = False
for k in range(n):
    print(k, '-','prostoe' if a[k] else 'sostavnoe')
'''
number = 1000 + 1
def mult (number):
    natural = []
    for x in range (1, number):
        if x % 3 == 0:
            natural.append(x)
        elif x % 5 == 0:
            natural.append(x)
        else:
            pass
    return natural

print(mult(number))
sum_it = mult(number)
print(sum(sum_it))
