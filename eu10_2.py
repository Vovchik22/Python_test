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
