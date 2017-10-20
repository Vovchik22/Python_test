'''
total_sum = 0
for i in range(1, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        total_sum = total_sum + i
print (total_sum)


a = sum(range(0, 1000, 3))
b = sum(range(0, 1000, 5))
c = sum(range(0, 1000, 15))
x = a + b - c
print(x)
'''
'''
print(sum([i for i in range(1,1000) if (i % 3 == 0 or i % 5 == 0)]))
'''
'''
[a+b for a in [1,2,3] for b in [4,5,6] ]
'''

'''
not_primes, lim = set(), 2000000
s = 0
for i in range(2,lim):
  if i not in not_primes:
    s += i
    for j in range(2*i, lim, i):
      not_primes.add(j)

print(s)
'''
